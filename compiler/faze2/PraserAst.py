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


class MyException2(Exception):
    def __init__(self, message, res, followed_string):
        self.message = message
        self.followed_string = followed_string
        self.res = res
        super().__init__(message)


class PraserAst:
    action = None
    params = None

    def __init__(self, action=None, params=None, return_line=None):
        self.action = action
        self.params = params
        self.return_line = return_line

    def execute(self):
        result = None

        if self.action == "function":  # TYPE ID  flist body/expr
            if self.params[1] in idenInfo.keys():
                print("### Semantic Error ###")
                print("function", self.params[1], "already exist!\n")

            else:
                symbol = SymbolTable(
                    self.params[1],
                    self.params[0],
                    True,
                    False,
                    False,
                    len(self.params[2]) if self.params[2] else 0,
                )

                if self.params[2] != None:
                    [symbol.add_parameter(x[1]) for x in self.params[2]]
                    [symbol.add_parameter_type(x[0]) for x in self.params[2]]

                idenInfo[self.params[1]] = symbol

                result = symbol.name

        # ID TYPE
        elif self.action == "func_arguman":
            symbol = SymbolTable(
                self.params[0],
                self.params[1],
                False,
                True,
                False,
                0,
            )

            symbol.is_assigned_value = True
            symbol.assign_value(self.params[1])
            result = symbol.value

            idenInfo[self.params[0]] = symbol

            # result = [(self.params[0], self.params[1])]

        elif self.action == "type_check":
            valid_types = ["str", "int", "null", "vector"]

            if self.params[0] in valid_types:
                print("unaxpected type of identifire")
            else:
                result = self.params[0]

        elif self.action == "return_type":
            if type(self.params[0]).__name__ != self.params[1]:
                print(
                    "### semantic error ###\nfunction return type does not match with what it actually returns!\n"
                )

        # stack expr
        elif self.action == "return_type2":
            for item in self.params[0]:
                if isinstance(item, LexToken) and item.type == "ID":
                    function_name = item.value
                    break

            for item in self.params[0]:
                if item.type == "type":
                    function_reutrn_type = item.value

            if isinstance(self.params[1], int):
                what_function_reutrns = type(self.params[1]).__name__
            else:
                if self.params[1] in idenInfo:
                    what_function_reutrns = idenInfo[self.params[1]].var_type
                else:
                    raise ValueError(f"Unknown variable name: {self.params[1]}")

            if function_reutrn_type != what_function_reutrns:
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
                    function_name,
                    Style.RESET_ALL,
                    "wrong return type expected",
                    function_reutrn_type,
                    "but returned",
                    what_function_reutrns,
                    "instead.\n",
                )

            # raise Exception(self.params[1], "return")
            # raise MyException("semantic error", , self.params[1])
            # raise MyException("semantic error", self.params[1], "return")

        elif self.action == "condition":
            if self.params[0]:
                result = self.params[1]
            elif len(self.params) > 2:
                result = self.params[2]

        elif self.action == "while":
            while self.params[0]:
                result = self.params[1]

        elif self.action == "for":
            symbol = SymbolTable(
                self.params[0],
                None,
                False,
                False,
                False,
                0,
            )
            idenInfo[self.params[0]] = symbol

            for i in range(self.params[1], self.params[2]):
                result = self.params[3]

        # ID TYPE
        elif self.action == "declare":
            # type_list = ["str", "int", "null", "vector"]
            # if self.params[1] not in type_list:
            #     print("wrong type", "types must be one of the following", type_list)
            symbol = SymbolTable(
                self.params[0],
                self.params[1],
                False,
                False,
                False,
                0,
            )
            idenInfo[self.params[0]] = symbol
            result = idenInfo[self.params[0]].value  # .value ??????

        # ID, expr, p.stack, return_line
        elif self.action == "assign":  # identifire declared, now want to get value
            # [$end, LexToken(DEF,'def',21,190), LexToken(TYPE,'int',21,194), LexToken(ID,'main',21,198), LexToken(LPAREN,'(',21,202), flist, LexToken(RPAREN,')',21,203), LexToken(LBRACE,'{',21,205), stmt, stmt]

            for item in self.params[2]:
                if isinstance(item, LexToken) and item.type == "ID":
                    function_name = item.value
                    break

            #  and idenInfo[item.value].is_function

            var = None
            for x in idenInfo:
                if (
                    idenInfo[x].name == self.params[0]
                    and not idenInfo[x].is_function
                    and not idenInfo[x].is_argumman
                ):
                    var = idenInfo[x]
                    break

            if var:
                if type(self.params[1]).__name__ == var.var_type:
                    # if var.is_array:
                    #     var.value = idenInfo[x].value[self.params[1]]
                    # else:
                    var.is_assigned_value = True
                    var.assign_value(self.params[1])
                    result = var.value
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
                        "functoin",
                        Fore.YELLOW,
                        function_name,
                        Style.RESET_ALL,
                        ": variable",
                        var.name,
                        "expected to be of type",
                        type(self.params[1]).__name__
                        if type(self.params[1]).__name__ != "list"
                        else "vector",
                        "but it is",
                        var.var_type,
                        "instead\n",
                    )
            else:
                print("### semantic error ###\nvariable has not been declared yet")

        # ID TYPE expr
        elif self.action == "declare_assign":
            if type(self.params[2]).__name__ == self.params[1]:
                symbol = SymbolTable(
                    self.params[0],
                    self.params[1],
                    False,
                    False,
                    True if isinstance(self.params[2], (list)) else False,
                    0,
                )

                symbol.is_assigned_value = True
                symbol.assign_value(self.params[2])

                idenInfo[self.params[0]] = symbol
                result = idenInfo[self.params[0]].value

            else:
                print(
                    "### semantic error ###\nvariable",
                    self.params[0],
                    "should assign",
                    self.params[1],
                    "but given",
                    type(self.params[2]).__name__,
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
        elif self.action == "FunctoinCall":
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
