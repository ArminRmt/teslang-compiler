import re
from SymbolTable import SymbolTable

from ply.lex import LexToken
from colorama import init

init()
from colorama import Fore, Style, Back


idenInfo = []
return_call = []


class PraserAst:
    action = None
    params = None

    def __init__(self, action=None, params=None, return_line=None, stack=None):
        self.action = action
        self.params = params
        self.return_line = return_line
        self.stack = stack

    def execute(self):
        result = None

        def find_function_symbol(name):
            for i in range(len(idenInfo)):
                if idenInfo[i].is_function and idenInfo[i].name == name:
                    return idenInfo[i]

        def find_array_symbol(name):
            for i in range(len(idenInfo)):
                if idenInfo[i].name == name and idenInfo[i].is_array:
                    return idenInfo[i]

        def find_expr_symbol(name, count):
            if isinstance(name, int):
                return name
            else:
                for i in range(len(idenInfo)):
                    if (
                        idenInfo[i].scope == count
                        and idenInfo[i].name == name
                        and not idenInfo[i].is_function
                        and not idenInfo[i].is_argumman
                        and not idenInfo[i].is_array
                    ):
                        return idenInfo[i]

        def find_symbol(name, count):
            symbol = find_function_symbol(name)
            if symbol:
                return symbol
            symbol = find_expr_symbol(name, count)
            if symbol:
                return symbol
            symbol = find_array_symbol(name)
            if symbol:
                return symbol

        if self.action == "function":
            f_type, f_name, f_args, f_body = (
                self.params[0],
                self.params[1],
                self.params[2],
                self.params[3],
            )

            flag = False
            functoin_name = find_symbol(f_name, 0)

            if functoin_name:
                flag = True

            if flag:
                error_message = (
                    f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                    f"function {Fore.YELLOW}{f_name}{Style.RESET_ALL} already exists!\n"
                )
                print(error_message)

            else:
                function_symbol = SymbolTable(
                    name=f_name,
                    var_type=f_type,
                    is_function=True,
                    is_argumman=False,
                    is_array=False,
                    num_params=len(f_args) if f_args else 0,
                )

                if f_args:
                    [function_symbol.add_parameter(x[1]) for x in f_args]
                    [function_symbol.add_parameter_type(x[0]) for x in f_args]

                idenInfo.append(function_symbol)

                result = f_name

        elif self.action == "func_arguman":
            arg_name, arge_type = (
                self.params[0],
                self.params[1],
            )

            arg_symbol = SymbolTable(
                name=arg_name,
                var_type=arge_type,
                is_function=False,
                is_argumman=True,
                is_array=False,
                num_params=0,
            )

            idenInfo.append(arg_symbol)

        elif self.action == "return_type":
            f_body, f_type = self.params[0], self.params[1]

            if type(f_body).__name__ != f_type:
                print(
                    "### semantic error ###\nfunction return type does not match with what it actually returns!\n"
                )

        elif self.action == "return_type2":
            p_stack, p_expr, return_line = (
                self.params[0],
                self.params[1],
                self.params[2],
            )

            for item in p_stack:
                if isinstance(item, LexToken) and item.type == "ID":
                    function_name = item.value
                    break

            for item in p_stack:
                if item.type == "type":
                    function_reutrn_type = item.value
                    break

            what_function_reutrns = None

            if isinstance(p_expr, int):
                what_function_reutrns = type(p_expr).__name__
            else:
                symbol = find_symbol(p_expr, 1)

                if symbol is None:
                    error_message = (
                        f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                        f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} "
                        f"function {Fore.YELLOW}{function_name}{Style.RESET_ALL} "
                        f"return varible {p_expr} doesn't even declared\n"
                    )
                    print(error_message)

                else:
                    if symbol.value is None:
                        error_message = (
                            f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                            f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} "
                            f"function {Fore.YELLOW}{function_name}{Style.RESET_ALL} "
                            f"return varible ( {p_expr} ) doesn't have value\n"
                        )

                        print(error_message)

                    what_function_reutrns = symbol.var_type

            if function_reutrn_type != what_function_reutrns:
                error_message = (
                    f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                    f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} "
                    f"function {Fore.YELLOW}{function_name}{Style.RESET_ALL} "
                    f"wrong return type expected {function_reutrn_type} "
                    f"but returned {what_function_reutrns} instead.\n"
                )
                print(error_message)

            else:
                return_var = find_symbol(p_expr, 1)
                if return_var is not None:
                    if isinstance(return_var, int):
                        return_call.append([function_name, return_var])
                    else:
                        return_call.append([function_name, return_var.value])

        elif self.action == "condition":
            p_cond, p_stmt = self.params[0], self.params[1]
            if p_cond:
                result = p_stmt
            elif len(self.params) > 2:
                p_else_stmt = self.params[2]
                result = p_else_stmt

        elif self.action == "while":
            while_cond, while_stmt = self.params[0], self.params[1]
            while while_cond:
                result = while_stmt

        elif self.action == "for":
            loop_variable_name, loop_start, loop_end, loop_body = (
                self.params[0],
                self.params[1],
                self.params[2],
                self.params[3],
            )

            while loop_start < loop_end:
                result = loop_body
                loop_start += 1

        elif self.action == "declare":
            var_name, var_type = (
                self.params[0],
                self.params[1],
            )

            declare_symbol = SymbolTable(
                name=var_name,
                var_type=var_type,
                is_function=False,
                is_argumman=False,
                is_array=False,
                num_params=0,
            )

            idenInfo.append(declare_symbol)

        elif self.action == "assign":
            var_name, value_to_assign, parsing_stack, return_line = (
                self.params[0],
                self.params[1],
                self.params[2],
                self.params[3],
            )

            for item in parsing_stack:
                if isinstance(item, LexToken) and item.type == "ID":
                    function_name = item.value
                    break

            var = find_symbol(var_name, 1)

            if var is None:
                print(
                    f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                    f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} "
                    f"function {Fore.YELLOW}{function_name}{Style.RESET_ALL}: "
                    f"variable {var_name} has not been declared yet \n"
                )

            else:
                if type(value_to_assign).__name__ != var.var_type:
                    print(
                        f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                        f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} "
                        f"function {Fore.YELLOW}{function_name}{Style.RESET_ALL}: "
                        f"variable {var.name} expected to be of type "
                        f"{'vector' if type(value_to_assign).__name__ == 'list' else type(value_to_assign).__name__} "
                        f"but it is {var.var_type} instead\n"
                    )

                else:
                    var.is_assigned_value = True
                    var.assign_value(value_to_assign)
                    result = value_to_assign

        elif self.action == "declare_assign":
            var_name, var_type, var_value, p_stack = (
                self.params[0],
                self.params[1],
                self.params[2],
                self.params[3],
            )

            count = 0
            for item in p_stack[::-1]:
                if isinstance(item, LexToken) and item.type == "ID":
                    count += 1

            var_type = "list" if var_type == "vector" else var_type

            if type(var_value).__name__ != var_type:
                print(
                    "### semantic error ###\nvariable",
                    var_name,
                    "should assign",
                    var_type,
                    "but given",
                    type(var_value).__name__,
                )

            else:
                symbol = SymbolTable(
                    name=var_name,
                    var_type=var_type,
                    is_function=False,
                    is_argumman=False,
                    is_array=True if isinstance(var_value, (list)) else False,
                    num_params=0,
                    scope=count,
                )

                symbol.is_assigned_value = True
                symbol.assign_value(var_value)

                idenInfo.append(symbol)

                result = var_value

        elif self.action == "print":
            expr, p_stack = self.params[0], self.params[1]

            count = 0
            for item in p_stack[::-1]:
                if isinstance(item, LexToken) and item.type == "ID":
                    count += 1

            node = find_symbol(expr, count)

            if isinstance(node, int):
                print(f"---   print built-in method printed {node}   ---\n")
            elif node is not None:
                print(f"---   print built-in method printed {node.value}   ---\n")
            else:
                print("---   print built-in method printed (None)   ---\n")

        elif self.action == "builtin_length":
            array = self.params[0]
            node = find_symbol(array, 0)
            if node:
                result = int(len(node.value))
            else:
                print(f"{array} hasn't been declared")

        elif self.action == "builtin_list":
            list_length = self.params[0]
            result = [None for _ in range(list_length)]

        elif self.action == "list_assignment":
            array_name, index, value, return_line = (
                self.params[0],
                self.params[1],
                self.params[2],
                self.params[3],
            )

            array_node = find_symbol(array_name, 0)

            if array_node is None:
                error_message = (
                    f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                    f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} "
                    f"Variable '{array_name}' is not an array "
                    f"or has not been declared yet\n"
                )
                print(error_message)

            else:
                array_node.value[index] = value

        elif self.action == "ArrayIndex":
            array_name, index, return_line = (
                self.params[0],
                self.params[1],
                self.params[2],
            )

            array_node = find_symbol(array_name, 0)

            if array_node is None:
                error_message = (
                    f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                    f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} "
                    f"Variable '{array_name}' is not an array\n"
                    f"or has not been declared yet\n"
                )
                print(error_message)

            else:
                result = array_node.value[index]

        elif self.action == "ListNode":
            list_elements = self.params[0]
            result = [int(e) for e in list_elements]

        elif self.action == "FunctionCall":
            func_name, func_args, return_line = (
                self.params[0],
                self.params[1],
                self.params[2],
            )

            func = find_symbol(func_name, 0)

            if func is None:
                error_message = (
                    f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                    f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} "
                    f"No such a function with name of {Fore.YELLOW}{func_name}{Style.RESET_ALL} exist!\n"
                )
                print(error_message)

            else:
                if return_call:
                    func.is_assigned_value = True
                    func.assign_value(return_call[0][1])
                    return_call.pop()

                if not func.num_params == len(func_args):
                    error_message = (
                        f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                        f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} Function: "
                        f"{Fore.YELLOW}{func.name}{Style.RESET_ALL} expects {func.num_params} arguments "
                        f"but got {len(func_args)}\n"
                    )
                    print(error_message)

                param_type_list = func.param_type_list

                for j_index, j in enumerate(func_args):
                    var = find_symbol(j, 1)
                    if isinstance(j, int):
                        if not type(j).__name__ in param_type_list:
                            arg_value = None
                            if isinstance(j, int) == False and var.value is not None:
                                arg_value = var.var_type
                            elif var.value is None:
                                arg_value = "null"
                            else:
                                arg_value = type(j).__name__

                            error_message = (
                                f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                                f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} Function: "
                                f"{Fore.YELLOW}{func.name}{Style.RESET_ALL} expected argument {j} "
                                f"to be of type {param_type_list[j_index]}, but it is {arg_value}\n"
                            )

                            print(error_message)

                    else:
                        if var:
                            if var.var_type != param_type_list[j_index]:
                                arg_value = None
                                if (
                                    isinstance(j, int) == False
                                    and var.value is not None
                                ):
                                    arg_value = var.var_type
                                elif var.value is None:
                                    arg_value = "null"
                                else:
                                    arg_value = type(j).__name__

                                error_message = (
                                    f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                                    f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} Function: "
                                    f"{Fore.YELLOW}{func.name}{Style.RESET_ALL} expected argument {j} "
                                    f"to be of type {param_type_list[j_index]}, but it is {arg_value}\n"
                                )

                                print(error_message)

                            if var.value is None and var.is_array:
                                error_message = (
                                    f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                                    f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} Function: "
                                    f"{Fore.YELLOW}{func.name}{Style.RESET_ALL} {j} "
                                    f"(value: null)\n"
                                )

                                print(error_message)

                        else:
                            print("variable doesn't have any value")

            result = func.value

        elif self.action == "thearnaryOp":
            condition, expr, else_expr = (
                self.params[0],
                self.params[1],
                self.params[2],
            )

            result = expr if condition else else_expr

        elif self.action == "UnaryNot":
            expr = self.params[0]
            var = find_symbol(expr, 0)
            result = var.value if var else not expr

        elif self.action == "logop":
            params = list(self.params)
            result = params.pop()
            while len(params) >= 2:
                prev = result
                op = params.pop()
                comp = params.pop()
                result = {
                    "&&": lambda a, b: (a and b),
                    "||": lambda a, b: (a or b),
                }[
                    op
                ](prev, comp)

        elif self.action == "binop":
            first_num = find_symbol(self.params[0], 1)
            second_num = find_symbol(self.params[2], 1)

            a = (
                self.params[0]
                if isinstance(self.params[0], int)
                else first_num.value
                if first_num is not None
                else None
            )

            b = (
                self.params[2]
                if isinstance(self.params[2], int)
                else second_num.value
                if second_num is not None
                else None
            )

            op = self.params[1]

            for item in self.stack:
                if isinstance(item, LexToken) and item.type == "ID":
                    function_name = item.value
                    break

            if a is not None and b is not None:
                result = {
                    "+": lambda a, b: a + b,
                    "-": lambda a, b: a - b,
                    "*": lambda a, b: a * b,
                    "/": lambda a, b: a / b,
                    "%": lambda a, b: a % b,
                    "**": lambda a, b: a**b,
                    ">": lambda a, b: (a > b),
                    ">=": lambda a, b: (a >= b),
                    "<": lambda a, b: (a < b),
                    "<=": lambda a, b: (a <= b),
                    "==": lambda a, b: (a == b),
                    "!=": lambda a, b: (a != b),
                }[op](a, b)

            else:
                variables = []
                for x in (self.params[0], self.params[2]):
                    if not isinstance(x, int):
                        symbol = find_symbol(x, 1)
                        if symbol is None:
                            variables.append(x)
                        elif symbol.value is None:
                            variables.append(symbol.name)

                error_message = (
                    f"{Fore.RED}### Semantic Error ###{Style.RESET_ALL}\n"
                    f"{Fore.GREEN}Line: {self.return_line}{Style.RESET_ALL} "
                    f"function {Fore.YELLOW}{function_name}{Style.RESET_ALL}"
                    f": Variables {variables} are used before being declared or wont even declared.\n"
                )
                print(error_message)

        return result

    def __str__(self):
        return "[AST] %s %s" % (self.action, ";".join(str(x) for x in self.params))
