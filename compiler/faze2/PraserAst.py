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
                    len(self.params[2]) if self.params[2] else 0,
                )

                if self.params[2] != None:
                    [symbol.add_parameter(x[1]) for x in self.params[2]]

                idenInfo[self.params[1]] = symbol

                # print(symbol)

        elif self.action == "return_type":
            if type(self.params[0]).__name__ != self.params[1]:
                print(
                    "### semantic error ###\nfunction return type does not match with what it actually returns!"
                )

        elif self.action == "return_type2":
            for item in self.params[0]:
                if isinstance(item, LexToken) and item.type == "TYPE":
                    function_retuen_type = item.value
                    break
            if function_retuen_type != type(self.params[1]).__name__:
                print(
                    "### semantic error ###\nfunction return type does not match with what it actually returns!"
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
                0,
            )
            idenInfo[self.params[0]] = symbol

            for i in range(self.params[1], self.params[2]):
                result = self.params[3]

        elif self.action == "assign":
            symbol = SymbolTable(
                self.params[0],
                self.params[1],
                False,
                False,
                0,
            )
            if len(self.params > 2):
                symbol.is_assigned_value = True
                symbol.assign_value(self.params[2])

            idenInfo[self.params[0]] = symbol

            result = idenInfo[self.params[0]]
            # result = idenInfo[self.params[0]].value

        elif self.action == "arguman_assign":
            symbol = SymbolTable(
                self.params[0],
                self.params[1],
                False,
                True,
                0,
            )
            idenInfo[self.params[0]] = symbol

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

        # elif self.action == "FunctoinCall":
        #     pass

        elif self.action == "Index":
            result = self.params[0][self.params[1]]

        elif self.action == "thearnaryOp":
            result = self.params[1] if self.params[0] else self.params[2]

        # elif self.action == "get":
        #     result = symbols.get(self.params[0], 0)

        elif self.action == "UnaryNot":
            result = not self.params[0]

        elif self.action == "ListNode":
            res = []
            for n in self.params[0]:
                res.append(n)

            result = res

        elif self.action == "logop":
            params = list(self.params)
            result = params.pop()
            while len(params) >= 2:
                prev = result
                op = params.pop()  # operator ("AND" or "OR")
                comp = params.pop()
                debug("[LOGOP]", prev, op, comp)
                result = {
                    "&&": lambda a, b: (a and b),
                    "||": lambda a, b: (a or b),
                }[
                    op
                ](prev, comp)

        elif self.action == "binop":
            a = self.params[0]
            b = self.params[2]
            op = self.params[1]
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
            print("Error, unsupported operation:", str(self))

        debug("Resolving", str(self), result)

        return result

    def __str__(self):
        return "[AST] %s %s" % (self.action, ";".join(str(x) for x in self.params))
