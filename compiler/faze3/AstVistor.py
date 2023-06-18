from SymbolTable import SymbolTable
from CodeGenerator import CodeGenerator


from ply.lex import LexToken
from colorama import init

init()
from colorama import Fore, Style, Back


idenInfo = []
return_call = []
move_iget_flag = True


class MyException(Exception):
    def __init__(self, message, res, followed_string):
        self.message = message
        self.followed_string = followed_string
        self.res = res
        super().__init__(message)
        # raise MyException("semantic error", , self.params[1])


class AstVistor:
    action = None
    params = None

    def __init__(self, action=None, params=None, return_line=None, stack=None):
        self.action = action
        self.params = params
        self.return_line = return_line
        self.stack = stack
        self.codegen = CodeGenerator()

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

        def find_arguman_symbol(name):
            for i in range(len(idenInfo)):
                if idenInfo[i].name == name and idenInfo[i].is_argumman:
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
            symbol = find_arguman_symbol(name)
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

            add_code = f"proc {f_name}:\n"
            self.codegen.add_code(add_code)
            # print(str(self.codegen))

            flag = False
            functoin_name = find_symbol(f_name, 0)

            if functoin_name:
                flag = True

            # TODO: it shouldnt run what is inside the function
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

            add_code = f"ret\n"
            self.codegen.add_code(add_code)

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

            # self.codegen.add_code("ret\n")
            # print(str(self.codegen))

            if function_reutrn_type != what_function_reutrns:
                error_message = (
                    f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                    f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} "
                    f"function {Fore.YELLOW}{function_name}{Style.RESET_ALL} "
                    f"wrong return type expected {function_reutrn_type} "
                    f"but returned {what_function_reutrns} instead.\n"
                )
                print(error_message)

            else:  # storing function return values, later used to update value field of function
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

        # elif self.action == "condition":
        #     p_cond, p_stmt = self.params[0], self.params[1]
        #     # Get the label names for the if and else blocks
        #     if_label = self.codegen.get_label("r0")
        #     end_label = self.codegen.get_label("r1")

        #     # Generate the code for the else block (if it exists)
        #     self.codegen.add_code(f"{if_label}:\n")
        #     if p_cond:
        #         result = p_stmt
        #     elif len(self.params) > 2:
        #         p_else_stmt = self.params[2]
        #         result = p_else_stmt
        #     # Add the end label
        #     self.codegen.add_code(f"{end_label}:\n")

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

            # for_symbol = SymbolTable(
            #     name=loop_variable_name,
            #     var_type=None,
            #     is_function=False,
            #     is_argumman=False,
            #     is_array=False,
            #     num_params=0,
            # )

            # idenInfo[loop_variable_name] = for_symbol
            # if loop_end.type()

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

        elif self.action == "assign":  # identifire declared, now want to get value
            var_name, value_to_assign, parsing_stack, return_line = (
                self.params[0],
                self.params[1],
                self.params[2],
                self.params[3],
            )

            # find function name from stack
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

            global move_iget_flag
            if move_iget_flag:
                temp_reg1 = self.codegen.get_temp_reg()  # r1

                add_code = f"mov {temp_reg1}, {var_value}\n"
                self.codegen.add_code(add_code)

            count = 0
            # [::-1] == .reverse() for finding function scope and dont get confliet wiht other scope
            for item in p_stack[::-1]:
                if isinstance(item, LexToken) and item.type == "ID":
                    count += 1

            var_type = (
                "list" if var_type == "vector" else var_type
            )  # when var_type is vector it should change to list

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
            # [::-1] == .reverse() for finding function scope and dont get confliet wiht other scope
            for item in p_stack[::-1]:
                if isinstance(item, LexToken) and item.type == "ID":
                    count += 1

            node = find_symbol(expr, count)

            # if isinstance(node, int):
            #     print(f"---   print built-in method printed {node}   ---\n")
            # elif node is not None:
            #     print(f"---   print built-in method printed {node.value}   ---\n")
            # else:
            #     print("---   print built-in method printed (None)   ---\n")

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

        elif self.action == "builtin_scan":
            move_iget_flag = False
            result = int(input("testing scan enter s.th\n"))
            temp_reg1 = self.codegen.get_temp_reg()  # r1
            add_code = f"call iget, {temp_reg1}\n"
            self.codegen.add_code(add_code)

        # ID expr expr
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

        # expr[expr]
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

        elif self.action == "ListNode":  # what if sting also be in list near int
            list_elements = self.params[0]
            result = [int(e) for e in list_elements]

        # ID, clist, return_line
        elif self.action == "FunctionCall":
            func_name, func_args, return_line = (
                self.params[0],
                self.params[1],
                self.params[2],
            )

            # register to store the return value
            ret_reg = self.codegen.get_temp_reg()
            arg_regs = []
            for arg in func_args:
                arg_reg = self.codegen.get_args_regs()
                # self.codegen.add_code(f"mov {arg_reg}, {arg}\n")
                arg_regs.append(arg_reg)

            # Generate the code to call the function and store the return value in ret_reg
            self.codegen.add_code(
                f"call {func_name}, {ret_reg}, {' '.join(arg_regs)}\n"
            )

            # Generate the code to move the return value to the return_line register
            self.codegen.add_code(f"mov {self.codegen.get_ret_reg()}, {ret_reg}\n")

            func = find_symbol(
                func_name, 0
            )  # 0 for finding in functino mehotd not expresstion

            # for i in range(len(func_args)):
            #     call_sym = find_symbol(func_args[i], 1)  # call function param
            #     func_sym = find_symbol(func.param_list[i], 0)  # declared funciotn param

            #     func_sym.assign_value(call_sym.value)

            if func is None:
                error_message = (
                    f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                    f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} "
                    f"No such a function with name of {Fore.YELLOW}{func_name}{Style.RESET_ALL} exist!\n"
                )
                print(error_message)

            else:
                # assigning function with acutally it returnes
                if return_call:
                    func.is_assigned_value = True
                    func.assign_value(return_call[0][1])
                    return_call.pop()

                # number of params wrong
                if not func.num_params == len(func_args):
                    error_message = (
                        f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                        f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} Function: "
                        f"{Fore.YELLOW}{func.name}{Style.RESET_ALL} expects {func.num_params} arguments "
                        f"but got {len(func_args)}\n"
                    )
                    print(error_message)

                # params type has mistakes
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
                            if (
                                var.var_type != param_type_list[j_index]
                            ):  # vartype not in functon type parms
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

                            if (
                                var.value is None and var.is_array
                            ):  # call varible not have valible
                                error_message = (
                                    f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                                    f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} Function: "
                                    f"{Fore.YELLOW}{func.name}{Style.RESET_ALL} {j} "
                                    f"(value: null)\n"
                                )

                                print(error_message)

                        else:
                            print("variable doesn't have any value")

            # func(*func_args)

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
            # result = not expr if isinstance(expr, int) else not var.value
            result = var.value if var else not expr

        elif self.action == "logop":
            params = list(self.params)
            result = params.pop()
            while len(params) >= 2:
                prev = result
                op = params.pop()  # operator ("&&" or "||")
                comp = params.pop()
                result = {
                    "&&": lambda a, b: (a and b),
                    "||": lambda a, b: (a or b),
                }[
                    op
                ](prev, comp)

        elif self.action == "binop":
            # finding varibles to be operated
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

            # what is our operation
            op = self.params[1]

            for item in self.stack:
                if isinstance(item, LexToken) and item.type == "ID":
                    function_name = item.value
                    break

            # and op in "+-*/%**><=" and type(a) == type(b) and type(a) in [int, float] and type(b) in [int, float]
            if a is not None and b is not None:
                # Get the register to store the result
                result_reg = self.codegen.get_temp_reg()
                result_reg1 = self.codegen.get_args_regs()
                result_reg2 = self.codegen.get_args_regs()

                # Generate the operation code
                if self.params[1] == "+":
                    self.codegen.add_code(
                        f"add {result_reg}, {result_reg1}, {result_reg2}\n"
                    )
                elif self.params[1] == "-":
                    self.add_code(f"sub {result_reg}, {result_reg1}, {result_reg2}\n")
                elif self.params[1] == "*":
                    self.add_code(f"mul {result_reg}, {result_reg1}, {result_reg2}\n")
                elif self.params[1] == "/":
                    self.add_code(f"div {result_reg}, {result_reg1}, {result_reg2}\n")
                elif self.params[1] == "%":
                    self.codegen.add_code(
                        f"mod {result_reg}, {result_reg1}, {result_reg2}\n"
                    )
                elif self.params[1] == "<":
                    self.codegen.add_code(
                        f"cmp< {result_reg}, {result_reg1}, {result_reg2}\n"
                    )
                elif self.params[1] == ">":
                    self.codegen.add_code(
                        f"cmp> {result_reg}, {result_reg1}, {result_reg2}\n"
                    )
                elif self.params[1] == "==":
                    self.codegen.add_code(
                        f"cmp== {result_reg}, {result_reg1}, {result_reg2}\n"
                    )
                elif self.params[1] == "<=":
                    self.codegen.add_code(
                        f"cmp<= {result_reg}, {result_reg1}, {result_reg2}\n"
                    )
                elif self.params[1] == ">=":
                    self.codegen.add_code(
                        f"cmp>= {result_reg}, {result_reg1}, {result_reg2}\n"
                    )

                move_iget_flag = False

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
                #  print varibles that used before being declared or wont even declared
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
