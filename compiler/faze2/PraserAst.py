DEBUG_MODE = False

from SymbolTable import SymbolTable
from ply.lex import LexToken
from colorama import init

init()
from colorama import Fore, Style, Back


idenInfo = {}


def debug(*params):
    if DEBUG_MODE:
        print("[DBG] %s" % (" : ".join(str(x) for x in params),))


class MyException(Exception):
    def __init__(self, message, res, followed_string):
        self.message = message
        self.followed_string = followed_string
        self.res = res
        super().__init__(message)
        # raise MyException("semantic error", , self.params[1])


class PraserAst:
    action = None
    params = None

    def __init__(self, action=None, params=None, return_line=None):
        self.action = action
        self.params = params
        self.return_line = return_line

    def execute(self):
        result = None

        def find_symbol(is_what, func_name):
            if is_what == "is_function":
                functions = {f.name: f for f in idenInfo.values() if f.is_function}
            elif is_what == "is_array":
                functions = {f.name: f for f in idenInfo.values() if f.is_array}
            else:
                functions = {
                    f.name: f
                    for f in idenInfo.values()
                    if not f.is_function and not f.is_argumman
                }

            func = functions.get(func_name)

            return func

        if self.action == "function":
            f_type, f_name, f_args, f_body = (
                self.params[0],
                self.params[1],
                self.params[2],
                self.params[3],
            )

            if f_name in idenInfo.keys():
                error_message = (
                    f"### Semantic Error ###\nFunction '{f_name}' already exists!\n"
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

                idenInfo[f_name] = function_symbol

                result = function_symbol.name

        elif self.action == "func_arguman":
            arg_value, arge_type = (
                self.params[0],
                self.params[1],
            )

            arg_symbol = SymbolTable(
                name=arg_value,
                var_type=arge_type,
                is_function=False,
                is_argumman=True,
                is_array=False,
                num_params=0,
            )

            arg_symbol.is_assigned_value = True
            arg_symbol.assign_value(arge_type)

            idenInfo[self.params[0]] = arg_symbol

            result = arg_symbol.value

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

            if isinstance(p_expr, int):
                what_function_reutrns = type(p_expr).__name__
            else:
                if p_expr in idenInfo:
                    what_function_reutrns = idenInfo[p_expr].var_type
                else:
                    raise ValueError(f"Unknown variable name: {p_expr}")

            if function_reutrn_type != what_function_reutrns:
                error_message = (
                    f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                    f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} "
                    f"function {Fore.YELLOW}{function_name}{Style.RESET_ALL} "
                    f"wrong return type expected {function_reutrn_type} "
                    f"but returned {what_function_reutrns} instead.\n"
                )
                print(error_message)

        elif self.action == "condition":
            if self.params[0]:
                result = self.params[1]
            elif len(self.params) > 2:
                result = self.params[2]

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

            for_symbol = SymbolTable(
                name=loop_variable_name,
                var_type=None,
                is_function=False,
                is_argumman=False,
                is_array=False,
                num_params=0,
            )

            idenInfo[loop_variable_name] = for_symbol

            loop_index = loop_start
            while loop_index < loop_end:
                result = loop_body
                loop_index += 1

        elif self.action == "declare":
            var_name, var_type = (
                self.params[0],
                self.params[1],
            )
            # type_list = ["str", "int", "null", "vector"]
            # if self.params[1] not in type_list:
            #     print("wrong type", "types must be one of the following", type_list)

            declare_symbol = SymbolTable(
                name=var_name,
                var_type=var_type,
                is_function=False,
                is_argumman=False,
                is_array=False,
                num_params=0,
            )

            idenInfo[var_name] = declare_symbol
            result = idenInfo[var_name].value  # .value ??????

        elif self.action == "assign":  # identifire declared, now want to get value
            var_name, var_value, parsing_stack, return_line = (
                self.params[0],
                self.params[1],
                self.params[2],
                self.params[3],
            )

            for item in parsing_stack:
                if isinstance(item, LexToken) and item.type == "ID":
                    function_name = item.value
                    break

            var = None
            for x in idenInfo:
                if (
                    idenInfo[x].name == var_name
                    and not idenInfo[x].is_function
                    and not idenInfo[x].is_argumman
                ):
                    var = idenInfo[x]
                    break

            if not var:
                print("### semantic error ###\nvariable has not been declared yet")

            if type(var_value).__name__ != var.var_type:
                print(
                    f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                    f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} "
                    f"function {Fore.YELLOW}{function_name}{Style.RESET_ALL}: "
                    f"variable {var.name} expected to be of type "
                    f"{'vector' if type(var_value).__name__ == 'list' else type(var_value).__name__} "
                    f"but it is {var.var_type} instead\n"
                )

            else:
                var.is_assigned_value = True
                var.assign_value(var_value)
                result = var.value

        elif self.action == "declare_assign":
            var_name, var_type, var_value = (
                self.params[0],
                self.params[1],
                self.params[2],
            )

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
                declare_assign_symbol = SymbolTable(
                    name=var_name,
                    var_type=var_type,
                    is_function=False,
                    is_argumman=False,
                    is_array=True if isinstance(var_value, (list)) else False,
                    num_params=0,
                )

                declare_assign_symbol.is_assigned_value = True
                declare_assign_symbol.assign_value(var_value)

                idenInfo[var_name] = declare_assign_symbol
                result = idenInfo[var_name].value

        elif self.action == "print":
            print(" ".join(str(x) for x in list(self.params)))

        elif self.action == "builtin_length":
            restult = len(self.params[0])

        # ID expr expr
        elif self.action == "list_assignment":
            array_name, index, value, return_line = (
                self.params[0],
                self.params[1],
                self.params[2],
                self.params[3],
            )

            if array_name not in idenInfo:
                print("### semantic error ###\nvariable has not been declared yet")

            if not idenInfo[array_name].is_array:
                error_message = (
                    f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                    f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} "
                    f"Variable '{array_name}' is not an array\n"
                )
                print(error_message)

            else:
                for x in idenInfo:
                    if idenInfo[x].is_array and idenInfo[x].name == array_name:
                        idenInfo[array_name].value[index] = value
                        break

        # expr[expr]
        elif self.action == "ArrayIndex":
            array_name, index, return_line = (
                self.params[0],
                self.params[1],
                self.params[2],
            )

            if array_name not in idenInfo:
                print("### semantic error ###\nvariable has not been declared yet")

            if not idenInfo[array_name].is_array:
                error_message = (
                    f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                    f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} "
                    f"Variable '{array_name}' is not an array\n"
                )
                print(error_message)

            else:
                for x in idenInfo:
                    if idenInfo[x].is_array and idenInfo[x].name == array_name:
                        result = idenInfo[x].value[index]
                        break

        elif self.action == "builtin_list":
            list_length = self.params[0]
            result = [None for _ in range(list_length)]

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

            func = find_symbol("is_function", func_name)

            if not func:
                error_message = "### semantic error ###\nNo such a function exist!"
                print(error_message)

            else:
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
                    if isinstance(j, int):
                        if not type(j).__name__ in param_type_list:
                            arg_value = None
                            if (
                                isinstance(j, int) == False
                                and idenInfo[j].value is not None
                            ):
                                arg_value = idenInfo[j].var_type
                            elif idenInfo[j].value is None:
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
                        var = find_symbol("noFunc_noArgs", j)

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

        elif self.action == "thearnaryOp":
            condition, expr, else_expr = (
                self.params[0],
                self.params[1],
                self.params[2],
            )
            result = expr if condition else else_expr

        # elif self.action == "get":
        #     result = symbols.get(self.params[0], 0)

        elif self.action == "UnaryNot":
            expr = self.params[0]
            result = not expr if isinstance(expr, int) else not idenInfo[expr].value

        elif self.action == "logop":
            params = list(self.params)
            result = params.pop()
            while len(params) >= 2:
                prev = result
                op = params.pop()  # operator ("&&" or "||")
                comp = params.pop()
                debug("[LOGOP]", prev, op, comp)
                result = {
                    "&&": lambda a, b: (a and b),
                    "||": lambda a, b: (a or b),
                }[
                    op
                ](prev, comp)

        elif self.action == "binop":
            a = (
                self.params[0]
                if isinstance(self.params[0], int)
                else idenInfo[self.params[0]].value
            )

            op = self.params[1]

            b = (
                self.params[2]
                if isinstance(self.params[2], int)
                else idenInfo[self.params[2]].value
            )

            # for item in self.params[2:]:
            #     if isinstance(item, LexToken) and item.type == "ID":
            #         function_name = item.value
            #         break

            # and op in "+-*/%**><=" and type(a) == type(b) and type(a) in [int, float] and type(b) in [int, float]
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
                debug("[BINOP]", a, op, b, result)

            else:
                variables = [
                    x
                    for x in (self.params[0], self.params[2])
                    if not isinstance(x, int) and not idenInfo[x].is_argumman
                ]
                error_message = (
                    f"{Fore.RED}### Semantic Error ###{Style.RESET_ALL}\n"
                    f"{Fore.GREEN}Line: {self.return_line}{Style.RESET_ALL}"
                    f"function {Fore.YELLOW}find{Style.RESET_ALL}"
                    f": Variables {variables} are used before being assigned.\n"
                )
                print(error_message)

        debug("Resolving", str(self), result)

        return result

    def __str__(self):
        return "[AST] %s %s" % (self.action, ";".join(str(x) for x in self.params))
