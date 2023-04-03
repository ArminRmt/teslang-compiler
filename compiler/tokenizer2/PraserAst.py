DEBUG_MODE = False

from SymbolTable import SymbolTable

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
            symbol = SymbolTable(
                self.params[1],
                self.params[0],
                True,
                False,
                len(self.params[2]),
            )

            [symbol.add_parameter(x[1]) for x in self.params[2]]

            idenInfo[self.params[1]] = symbol

        elif self.action == "condition":
            if PraserAst.resolve(self.params[0]):
                result = PraserAst.resolve(self.params[1])
            elif len(self.params) > 2:
                result = PraserAst.resolve(self.params[2])

        elif self.action == "while":
            while PraserAst.resolve(self.params[0]):
                PraserAst.resolve(self.params[1])

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
                PraserAst.resolve(self.params[3])

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
                symbol.assign_value(PraserAst.resolve(self.params[2]))

            idenInfo[self.params[0]] = symbol

            result = idenInfo[self.params[0]].value

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
            print(" ".join(str(PraserAst.resolve(x)) for x in list(self.params)))

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
            result = PraserAst.resolve(self.params[0])[
                PraserAst.resolve(self.params[1])
            ]

        elif self.action == "thearnaryOp":
            result = (
                ParserAst.resolve(self.params[1])
                if ParserAst.resolve(self.params[0])
                else ParserAst.resolve(self.params[2])
            )

        # elif self.action == "get":
        #     result = symbols.get(self.params[0], 0)

        elif self.action == "UnaryNot":
            result = not PraserAst.resolve(self.params[0])

        elif self.action == "ListNode":
            res = []
            for n in self.params[0]:
                res.append(PraserAst.resolve(n))

            result = res

        elif self.action == "logop":
            params = list(self.params)
            result = PraserAst.resolve(params.pop())
            while len(params) >= 2:
                prev = result
                op = PraserAst.resolve(params.pop())  # operator ("AND" or "OR")
                comp = PraserAst.resolve(params.pop())
                debug("[LOGOP]", prev, op, comp)
                result = {"&&": lambda a, b: (a and b), "||": lambda a, b: (a or b),}[
                    op
                ](prev, comp)

        elif self.action == "binop":
            a = PraserAst.resolve(self.params[0])
            b = PraserAst.resolve(self.params[2])
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

    # True if x is not None and if x is an instance of the PraserAst Otherwise, False.
    @staticmethod
    def isADelayedAction(x=None):
        return "x" != None and isinstance(x, PraserAst)

    @staticmethod
    def resolve(x):
        if not PraserAst.isADelayedAction(x):
            return x
        else:
            return x.execute()
