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

        if self.action == "function":
            f_type, f_name, f_args, f_body = (
                self.params[0],
                self.params[1],
                self.params[2],
                self.params[3],
            )

            if f_name in idenInfo.keys():
                print("### Semantic Error ###")
                print("function", f_name, "already exist!\n")

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
                return
            else:
                if type(var_value).__name__ != var.var_type:
                    print(
                        f"{Fore.RED}### semantic error ###{Style.RESET_ALL}\n"
                        f"{Fore.GREEN}Line: {return_line}{Style.RESET_ALL} "
                        f"function {Fore.YELLOW}{function_name}{Style.RESET_ALL}: "
                        f"variable {var.name} expected to be of type "
                        f"{'vector' if type(var_value).__name__ == 'list' else type(var_value).__name__} "
                        f"but it is {var.var_type} instead\n"
                    )
                    return

                var.is_assigned_value = True
                var.assign_value(var_value)
                result = var.value

        elif self.action == "declare_assign":
            var_name, var_type, var_value = (
                self.params[0],
                self.params[1],
                self.params[2],
            )

            if type(var_value).__name__ == var_type:
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

            else:
                print(
                    "### semantic error ###\nvariable",
                    var_name,
                    "should assign",
                    var_type,
                    "but given",
                    type(var_value).__name__,
                )

        elif self.action == "print":
            print(" ".join(str(x) for x in list(self.params)))

        elif self.action == "builtin_length":
            restult = len(self.params[0])

        # ID expr expr
        elif self.action == "list_assignment":
            if self.params[0] in idenInfo:
                if idenInfo[self.params[0]].is_array:
                    for x in idenInfo:
                        if idenInfo[x].is_array and idenInfo[x].name == self.params[0]:
                            idenInfo[self.params[0]].value[
                                self.params[1]
                            ] = self.params[2]
                else:
                    print(
                        Fore.RED
                        + "### semantic error ###"
                        + Style.RESET_ALL
                        + "\n"
                        + Fore.GREEN
                        + "Line:",
                        self.params[3],
                        Style.RESET_ALL,
                        "variable",
                        self.params[0],
                        "is not an array\n",
                    )
            else:
                print("### semantic error ###\nvariable has not been declared yet")

        # expr[expr]
        elif self.action == "ArrayIndex":
            if self.params[0] in idenInfo:
                if idenInfo[self.params[0]].is_array:
                    for x in idenInfo:
                        if idenInfo[x].is_array and idenInfo[x].name == self.params[0]:
                            result = idenInfo[x].value[self.params[1]]
                            break

        # expr
        elif self.action == "builtin_list":
            res = []
            for i in range(self.params[0]):
                res.append(None)

            result = res

            # restult = list(range(int(self.params[0])))

        ##################################################################
        # clist
        elif self.action == "ListNode":
            res = []
            for n in self.params[0]:
                res.append(n)

            # idenInfo[self.params[0]].value = res
            result = res
        ##################################################################

        # ID, clist, return_line
        elif self.action == "FunctionCall":
            if not self.params[0] in idenInfo.keys():
                print(
                    "### semantic error ###\nNo such a function exist!",
                )
            else:
                for x in idenInfo:
                    if idenInfo[x].is_function and idenInfo[x].name == self.params[0]:
                        f = idenInfo[x]
                # f = next((idenInfo[x] for x in idenInfo if callable(idenInfo[x]) and idenInfo[x].__name__ == self.params[0]), None)

                # func_params = f.get_parameter()
                # for x in func_params:
                #     symbol = SymbolTable(
                #         x,
                #         type(x),
                #         False,
                #         True,
                #         False,
                #         0,
                #     )
                #     symbol.is_assigned_value = True
                #     symbol.assign_value(x)
                #     idenInfo[x] = symbol

                # number of params wrong
                if not f.num_params == len(self.params[1]):
                    print(
                        Fore.RED
                        + "### semantic error ###"
                        + Style.RESET_ALL
                        + "\n"
                        + Fore.GREEN
                        + "Line:",
                        self.params[2],
                        Style.RESET_ALL,
                        "functino:",
                        Fore.YELLOW,
                        f.name,
                        Style.RESET_ALL,
                        "expects",
                        f.num_params,
                        "arguments but got",
                        len(self.params[1]),
                        "\n",
                    )
                # params type has mistakes
                param_type_list = f.param_type_list
                # ['A', 'a']
                for j_index, j in enumerate(self.params[1]):
                    if isinstance(j, int):
                        if not type(j).__name__ in param_type_list:
                            print(
                                Fore.RED
                                + "### semantic error ###"
                                + Style.RESET_ALL
                                + "\n"
                                + Fore.GREEN
                                + "Line:",
                                self.params[2],
                                Style.RESET_ALL,
                                "function",
                                Fore.YELLOW,
                                f.name,
                                Style.RESET_ALL,
                                "expected",
                                j,
                                "to be of type of",
                                param_type_list[j_index],
                                "but it's given",
                                idenInfo[j].var_type  # if varible with value is given
                                if isinstance(j, int) == False
                                and idenInfo[j].value is not None
                                else "null"  # if varible without value is given
                                if idenInfo[j].value is None
                                else type(j).__name__,  # if numbe is given
                            )
                        # break
                    else:
                        for item in idenInfo:
                            if (
                                j == idenInfo[item].name
                                and not idenInfo[item].is_function
                                and not idenInfo[item].is_argumman
                                # and idenInfo[item].value is None
                            ):
                                var = idenInfo[item]
                                break

                        if var:
                            if (
                                var.var_type != param_type_list[j_index]
                            ):  # vartype not in functon type parms
                                print(
                                    Fore.RED
                                    + "### semantic error ###"
                                    + Style.RESET_ALL
                                    + "\n"
                                    + Fore.GREEN
                                    + "Line:",
                                    self.params[2],
                                    Style.RESET_ALL,
                                    "function",
                                    Fore.YELLOW,
                                    f.name,
                                    Style.RESET_ALL,
                                    "expected",
                                    j,
                                    "to be of type of",
                                    param_type_list[j_index],
                                    "but it's given",
                                    var.var_type  # if varible with value is given
                                    if isinstance(j, int) == False
                                    and var.value is not None
                                    else "null"  # if varible without value is given
                                    if var.value is None
                                    else type(j).__name__,  # if numbe is given
                                )
                                # break
                            if (
                                var.value is None and var.is_array
                            ):  # call varible not have valible
                                print(
                                    Fore.RED
                                    + "### semantic error ###"
                                    + Style.RESET_ALL
                                    + "\n"
                                    + Fore.GREEN
                                    + "Line:",
                                    self.params[2],
                                    Style.RESET_ALL,
                                    "function",
                                    Fore.YELLOW,
                                    f.name,
                                    Style.RESET_ALL,
                                    j,
                                    "is null",
                                )
                        else:
                            print("variable doesn't have any value")

                # f.name(self.params[1])

        elif self.action == "thearnaryOp":
            result = self.params[1] if self.params[0] else self.params[2]

        # elif self.action == "get":
        #     result = symbols.get(self.params[0], 0)

        elif self.action == "UnaryNot":
            result = (
                not self.params[0]
                if isinstance(self.params[0], int)
                else not idenInfo[self.params[0]].value
            )

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
                print(
                    Fore.RED
                    + "### semantic error ###"
                    + Style.RESET_ALL
                    + "\n"
                    + Fore.GREEN
                    + "Line:",
                    self.return_line,
                    Style.RESET_ALL,
                    "functoin",
                    Fore.YELLOW,
                    "find",
                    Style.RESET_ALL,
                    ": Variables",
                    [
                        x
                        for x in (self.params[0], self.params[2])
                        if isinstance(x, int) == False
                        and idenInfo[x].is_argumman == False
                        # if idenInfo[x].value is None
                    ],
                    "is used before being assigned.\n",
                )

                # raise MyException("semantic error", self.params[1], "=")

                # raise Exception(self.params[2], self.params[0])
                # raise MyException("semantic error", "=", self.params[0])

        debug("Resolving", str(self), result)

        return result

    def __str__(self):
        return "[AST] %s %s" % (self.action, ";".join(str(x) for x in self.params))
