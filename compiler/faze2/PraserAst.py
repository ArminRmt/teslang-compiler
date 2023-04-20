DEBUG_MODE = False

from SymbolTable import SymbolTable
from ply.lex import LexToken
from Mylexer import find_column

idenInfo = {}


def debug(*params):
    if DEBUG_MODE:
        print("[DBG] %s" % (" : ".join(str(x) for x in params),))


class PraserAst:
    action = None
    params = None

    def __init__(self, action=None, params=None):
        self.action = action
        self.params = params

    def execute(self):
        result = None

        if self.action == "function":  # TYPE ID  flist body/expr
            if self.params[1] in idenInfo.keys():
                print("### Semantic Error ###")
                print("function", self.params[1], "already exist!")

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

                # print(symbol)

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
                    "### semantic error ###\nfunction return type does not match with what it actually returns!"
                )

        # stack expr
        elif self.action == "return_type2":
            function_retuen_type = None
            # print(self.params[0][2].value)
            # for item in self.params[0]:
            #     if isinstance(item, LexToken) and item.type == "type":
            #         function_retuen_type = item.value
            #         break

            for item in self.params[0]:
                if isinstance(item, LexToken) and item.type == "ID":
                    function_name = item.value
                    break

            if function_retuen_type != type(self.params[1]).__name__:
                obj = None
                for item in idenInfo:
                    if idenInfo[item].name == self.params[1]:
                        obj = item
                        break

                print(vars(obj))

                print(
                    "### semantic error ###\nfunction",
                    function_name,
                    "wrong return type expected",
                    self.params[0][3].value,
                    "but returned",
                    # idenInfo[self.params[1]].var_type
                    # if isinstance(self.params[1], int) == False
                    # else type(self.params[1]).__name__,
                    # "instead.",
                )
                # print(
                #     f"\nunexpected token  at line {self.params[2].lineno}, column {find_column(self.params[2])}"
                # )

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
            type_list = ["str", "int", "null", "vector"]
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

        # ID expr
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
                    var.is_assigned_value = True
                    var.assign_value(self.params[1])
                    result = var.value
                else:
                    print(
                        "### semantic error ###\nfunctoin",
                        function_name,
                        ": variable",
                        var.name,
                        "expected to be of type",
                        type(self.params[1]).__name__
                        if type(self.params[1]).__name__ != "list"
                        else "vector",
                        "but it is",
                        var.var_type,
                        "instead",
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

        elif self.action == "builtin_list":
            res = []
            for i in range(self.params[0]):
                res.append(None)
            result = res

            # restult = list(range(int(self.params[0])))

        # ID clist
        elif self.action == "FunctoinCall":
            if not self.params[0] in idenInfo.keys():
                print("### semantic error ###\nNo such a function exist!")
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
                        "### semantic error ###\nfunction",
                        f.name,
                        "expects",
                        f.num_params,
                        "arguments but got",
                        len(self.params[1]),
                    )
                # params type has mistakes
                param_type_list = f.param_type_list
                # ['A', 'a']
                for j_index, j in enumerate(self.params[1]):
                    if not type(j).__name__ in param_type_list:
                        print(
                            "### semantic error ###\nfunction",
                            f.name,
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

                # f.name(self.params[1])

        # expr[expr]
        elif self.action == "ArrayIndex":
            for x in idenInfo:
                if idenInfo[x].is_array and idenInfo[x].name == self.params[0]:
                    result = idenInfo[x].value[self.params[1]]
                    break

        # clist
        elif self.action == "ListNode":
            res = []
            for n in self.params[0]:
                res.append(n)

            result = res

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
                    "### semantic error ###\nfunctoin",
                    "find",
                    ": Variables",
                    [
                        x
                        for x in (self.params[0], self.params[2])
                        if isinstance(x, int) == False
                        and idenInfo[x].is_argumman == False
                        # if idenInfo[x].value is None
                    ],
                    "is used before being assigned.",
                )

        debug("Resolving", str(self), result)

        return result

    def __str__(self):
        return "[AST] %s %s" % (self.action, ";".join(str(x) for x in self.params))
