symbol_table = dict()


class Node:
    def __init__(self):
        pass

    def evaluate(self):  # traverse the AST and execute each statement in the program
        return 0  # indicates that the evaluation was successful.

    def execute(self):  # execute a single statement or expression in the program
        return 0


class BlockNode(Node):
    def __init__(self, s):
        self.s1 = [s]

    def execute(self):
        for statement in self.s1:
            statement.execute()


class ExpressionNode(Node):
    def evaluate(self):
        return None


class IntNode(ExpressionNode):
    def __init__(self, val):
        self.val = int(val)

    def evaluate(self):
        return self.val

    def __str__(self):
        return str(self.val)


class RealNode(ExpressionNode):
    def __init__(self, val):
        self.val = float(val)

    def evaluate(self):
        return self.val

    def __str__(self):
        return str(self.val)


class BoolNode(ExpressionNode):
    def __init__(self, val):
        self.val = val

    def evaluate(self):
        return self.val


class StringNode(ExpressionNode):
    def __init__(self, val):
        self.val = val

    def evaluate(self):
        return self.val


class ExpNode(ExpressionNode):
    def __init__(self, base, expo):
        self.base = base
        self.expo = expo

    def evaluate(self):
        return self.base.evaluate() ** self.expo.evaluate()


class ListNode(ExpressionNode):
    def __init__(self, val):
        self.val = val

    def evaluate(self):
        res = []
        for n in self.val:
            res.append(n.evaluate())
        return res


class IndexNode(ExpressionNode):
    def __init__(self, obj, ind):
        self.obj = obj
        self.ind = ind

    def evaluate(self):
        return self.obj.evaluate()[self.ind.evaluate()]


class UnaryOpNode(ExpressionNode):
    def __init__(self, op, val):
        self.op = op
        self.val = val

    def evaluate(self):
        return -self.value.evaluate()


class UnaryNotNode(ExpressionNode):
    def __init__(self, op, val):
        self.op = op
        self.val = val

    def evaluate(self):
        return not self.val.evaluate()


class BoolOpNode(ExpressionNode):
    def __init__(self, op, v1, v2):
        self.op = op
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        if self.op.vid == "and":
            res = self.v1.evaluate() and self.v2.evaluate()
        elif self.op.vid == "or":
            res = self.v1.evaluate() or self.v2.evaluate()
        return res


class BinOpNode(ExpressionNode):
    def __init__(self, op, v1, v2):
        self.op = op
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        if self.op == "+":
            return self.v1.evaluate() + self.v2.evaluate()
        elif self.op == "-":
            return self.v1.evaluate() - self.v2.evaluate()
        elif self.op == "*":
            return self.v1.evaluate() * self.v2.evaluate()
        elif self.op == "/":
            return self.v1.evaluate() / self.v2.evaluate()
        elif self.op == "%":
            return self.v1.evaluate() % self.v2.evaluate()
        elif self.op == "//":
            return self.v1.evaluate() // self.v2.evaluate()


class CompNode(ExpressionNode):
    def __init__(self, op, v1, v2):
        self.op = op
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        if self.op == "<":
            return self.v1.evaluate() < self.v2.evaluate()
        elif self.op == "<=":
            return self.v1.evaluate() <= self.v2.evaluate()
        elif self.op == "==":
            return self.v1.evaluate() == self.v2.evaluate()
        elif self.op == "!=":
            return self.v1.evaluate() != self.v2.evaluate()
        elif self.op == ">":
            return self.v1.evaluate() > self.v2.evaluate()
        elif self.op == ">=":
            return self.v1.evaluate() >= self.v2.evaluate()


class IDNode(ExpressionNode):
    def __init__(self, vid):
        self.vid = vid

    def evaluate(self):
        return symbol_table[self.vid]

    def __str__(self):
        return str(self.vid)


class ContainsNode(ExpressionNode):
    def __init__(self, obj, tgt):
        self.obj = obj
        self.tgt = tgt

    def evaluate(self):
        return self.obj.evaluate().__contains__(self.tgt.evaluate())


class StatementNode(Node):
    def execute(self):
        pass


class PrintNode(StatementNode):
    def __init__(self, exp):
        self.exp = exp

    def execute(self):
        print(str(self.exp.evaluate()))


class AssignNode(StatementNode):
    """defvar : VAR TYPE ID
    | VAR TYPE ID ASSIGN expr"""

    def __init__(self, type, vnode, exp=None):
        self.type = type
        self.vnode = vnode
        self.exp = exp

    def execute(self):
        if self.exp.evaluate() is not None:
            symbol_table[self.vnode.vid] = self.exp.evaluate()
        else:
            symbol_table[self.vnode.vid] = None


class AssignToListNode(StatementNode):
    def __init__(self, vnode, ind, exp):
        self.vnode = vnode
        self.exp = exp
        self.ind = ind

    def execute(self):
        symbol_table[self.vnode.vid][self.ind.evaluate()] = self.exp.evaluate()


class ForNode(StatementNode):
    def __init__(self, vid, start, end, stmt):
        self.vid = vid
        self.start = start
        self.end = end
        self.stmt = stmt

    def execute(self):
        for i in range(self.start, self.end).evaluate():
            self.stmt.execute()


class FuncNode(StatementNode):
    def __init__(self, type, vnode, flist, body, expr=None):
        self.type = type
        self.vnode = vnode
        self.flist = flist
        self.body = body
        self.expr = expr

    def execute(self):
        def func(*args):

            argument = []

            # Create a dictionary mapping argument names to values
            arg_dict = {arg.id: arg.evaluate() for arg in self.flist}

            # Add the arguments to the current environment
            for arg_name, arg_value in zip(arg_dict.keys(), args):
                argument.append([arg_name, arg_value])

            # Evaluate the function body
            self.body.evaluate()

            # Return the result of the function
            if self.expr.evaluate() is not None:
                return self.expr.evaluate()

        # Add the function to the current environment
        current_env().define(self.vid.id, func)
        symbol_table[self.vnode.vid] = func
        # symbol_table[self.vnode.vid] = [func, self.type, argument]


# ID LPAREN clist RPAREN
class FunctionCallNode(StatementNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def execute(self):
        self.name.evaluate(self.args.evaluate())


# expr QUESTIONMARK expr COLON expr
class TernaryOperatorNode(StatementNode):
    def __init__(self, cond, expr1, expr2):
        self.cond = cond
        self.expr1 = expr1
        self.expr2 = expr2

    def execute(self):
        self.expr1.execute() if self.cond.evaluate() else self.expr2.execute()


class IfNode(StatementNode):
    def __init__(self, cond, block):
        self.cond = cond
        self.block = block

    def execute(self):
        if self.cond.evaluate():
            self.block.execute()


class IfElseNode(StatementNode):
    def __init__(self, cond, iblock, eblock):
        self.cond = cond
        self.iblock = iblock
        self.eblock = eblock

    def execute(self):
        if self.cond.evaluate():
            self.iblock.execute()
        else:
            self.eblock.execute()


class WhileNode(StatementNode):
    def __init__(self, cond, block):
        self.cond = cond
        self.block = block

    def execute(self):
        while self.cond.evaluate():
            self.block.execute()
