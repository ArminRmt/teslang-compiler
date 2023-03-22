import sys
import ply.lex as lex
import ply.yacc as yacc


symbol_table = dict()


class Node:
    def __init__(self):
        pass

    def evaluate(self):  # traverse the AST and execute each statement in the program
        return 0  # indicates that the evaluation was successful.

    def execute(self): # execute a single statement or expression in the program
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
              | VAR TYPE ID ASSIGN exp"""
              
    def __init__(self, vartype, vnode, exp=None):
        self.vartype = vartype
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
        for i in range(self.start,self.end).evaluate():
            self.stmt.execute()
            



class FuncNode(StatementNode):
    def __init__(self, vartype, vnode, flist, body, expr=None):
        self.vartype = vartype
        self.vnode = vnode
        self.flist = flist
        self.body = body
        self.expr = expr

    def execute(self):
        
        def self.vnode.evaluate()(*args):
    

        
        
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
        symbol_table[self.vnode.vid] =  self.vnode.evaluate()
        # symbol_table[self.vnode.vid] = [func, self.vartype, argument]
        


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


reserved = {
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "not": "NOT",
    "and": "AND",
    "or": "OR",
    "in": "IN",
    "print": "PRINT",
    "var": "VAR",
    "def": "DEF",
    "for": "FOR",
    "not": "NOT",
    "to": "TO",
    "return": "RETURN",
    "null": "NULL"
    'int' : 'INT',
    'str' : 'STRING',
    'vector' : 'VECTOR',
}

tokens = [
    "INT",
    "STRING",
    "REAL",
    "LPAREN",
    "RPAREN",
    "LBLOCK",
    "RBLOCK",
    "BOOL",
    "EXP",
    "MULT",
    "DIV",
    "MOD",
    "INTDIV",
    "ADD",
    "SUB",
    "LESS",
    "LESSEQ",
    "EQUAL",
    "NOTEQUAL",
    "GREATER",
    "GREATEREQ",
    "ASSIGN",
    "LBRACE",
    "RBRACE",
    "SEMI",
    "ID",
    "COMMENT",
    "TYPE",
    "COMMA",
    "COLON",
    "QUESTIONMARK",
    "TO",
] + list(reserved.values())

t_AND = r'and'
t_OR = r'\o\r'
t_TO = r'\t\o'
t_IF = r'\i\f'
t_COMMA = r","
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBLOCK = r"\["
t_RBLOCK = r"\]"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_MOD = r"%"
t_INTDIV = r"//"
t_ADD = r"\+"
t_SUB = r"\-"
t_MULT = r"\*"
t_DIV = r"\/"
t_EXP = r"\*\*"
t_LESS = r"<"
t_LESSEQ = r"<\="
t_EQUAL = r"\=\="
t_NOTEQUAL = r"!\="
t_GREATER = r">"
t_GREATEREQ = r">\="
t_ASSIGN = r"\="
t_SEMI = r";"
t_COLON = r":"
t_AND = r"\&\&"
t_OR = r"\|\|"
t_QUESTIONMARK = r"\?"
t_ignore = " \t\r\n\f\v\\"
# t_WHITESPACE = r'(\t|\s)+'
t_NOT = r"!"
t_TYPE = r"int|vector|string|null"
t_RETURN = r"return"


def t_REAL(token):       # float
    r"\d*(\d\.|\.\d)\d*"
    token.value = RealNode(token.value)
    return token


def t_INT(token):
    r"\d+"
    token.value = IntNode(token.value)
    return token


def t_STRING(token):
    # r'(\"[^\"]*\") | (\'[^\']*\')'
    r'"(?:\\.|[^"])*"'
    token.value = StringNode(token.value[1 : len(token.value) - 1])
    return token


def t_COMMENT(t):
    # r'(\\\\(.|\n)*?\\\\)'
    r"\#.*"
    # print(t.value + 'ignored')
    pass


def t_BOOL(token):
    r"True|False"
    token.value = BoolNode(token.value == "True")
    return token


def t_ID(token):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    token.type = reserved.get(token.value, "ID")
    token.value = IDNode(token.value)
    return token


def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")
    # t.lexer.lineno += len(t.value)


# def find_column(input, token):
#     line_start = input.rfind('\n', 0, token.lexpos) + 1
#     return (token.lexpos - line_start) + 1


"""
illegal character is encountered during lexical analysis
"""
def t_error(token):
    print("Illegal character '%s'" % token.value[0])
    token.lexer.skip(1)


"""
parser can determine how to parse expressions and create an abstract syntax tree that represents the structure of the input code.
precedence from low to high
"""
precedence = (
    (
        "right",
        "ASSIGN",
    ),  # expression on the right is evaluated first, and then assigned to the variable on the left
    ("left", "PRINT"),
    ("left", "OR"),  # logical operators decreesing precedence
    ("left", "AND"),
    ("left", "NOT"),
    ("left", "UNOT"),
    (
        "left",
        "LESS",
        "LESSEQ",
        "EQUAL",
        "NOTEQUAL",
        "GREATER",
        "GREATEREQ",
    ),  # comparison operators same precedence
    ("left", "IN"),
    ("left", "ADD", "SUB"),  # arithmetic operators same precedence
    ("left", "INTDIV"),  # //
    ("left", "UMINUS"),  # The unary minus operator, -.
    ("left", "MOD"),
    ("left", "MULT", "DIV"),
    ("right", "EXP"),  # The exponentiation operator, **.
    ("left", "LBLOCK"),  # {
    ("left", "LIST"),
    ("left", "INDEX"),
)


funcNames = ["scan", "print", "list", "length", "exit"]

# function with the same name has already been defined
def newFCheck(t):
    if t in funcNames:
        print("function", t, "already exist!")
        raise Exception
    else:
        funcNames.append(t)


def p_prog(p):
    """prog := | func prog"""
    if len(p) == 3:
        p[0] = [p[1], p[2]]


def p_func(p):
    """func : def TYPE ID LPAREN flist RPAREN LBRACE body RBRACE    +
            | def TYPE ID LPAREN flist RPAREN RETURN expr SEMI      +
    """

    newFCheck(p[3])

    p[0] = FuncNode(p[2], p[3], p[5], p[8])



def p_body(p):
    """body :
    | stmt body"""

    if len(p) == 3:
        p[0] = p[2]
        p[0].s1.insert(0, p[1])
    else:
        p[0] = BlockNode([])
        p[0].s1 = []


def p_smt(p):

    """
    stmt : expr SEMI									+
        | defvar SEMI                                   +
        | IF LPAREN expr RPAREN stmt                    +
        | IF LPAREN expr RPAREN stmt ELSE stmt			+
        | WHILE LPAREN expr RPAREN stmt					+
        | FOR LPAREN ID EQUAL expr TO expr RPAREN stmt  +?
        | RETURN expr SEMI                              +
        | LBRACE body RBRACE                            +
        | func                                          +
        how about beatuiful print statment
    """

    if len(p) == 2: # func
        p[0] = p[1]

    if len(p) == 3:  # expr SEMICOLON | defvar SEMICOLON
        p[0] = p[1]

    if len(p) == 4:  #  RETURN expr SEMI | LBRACE body RBRACE
        pass
        p[0] = p[2]

    if len(p) == 6:
        if p[2] == t_IF:  # IF LPAREN expr RPAREN stmt
            p[0] = IfNode(p[3], p[5])
        else:
            p[0] = WhileNode(p[3], p[5])

    if len(p) == 8:  # IF LPAREN expr RPAREN stmt ELSE stmt
        p[0] = IfElseNode(p[1].cond, p[1].block, p[3])
        

	if len(p) == 9: # FOR LPAREN ID EQUAL expr TO expr RPAREN stmt
		p[0] = ForNode(p[3], p[5], p[7],p[9])
  
  

def p_defvar(p):
    """defvar : VAR TYPE ID              +
              | VAR TYPE ID ASSIGN expr  +
    """
                      
    p[0] = AssignNode(p[2], p[3], p[5])    



def p_expr(p):
    """expr : expr LBLOCK expr RBLOCK       +
            | LBLOCK clist RBLOCK           +
            | expr QUESTIONMARK expr COLON expr  +
            | expr ADD expr			+
            | expr SUB expr			+
            | expr MULT expr		+
            | expr DIV expr			+
            | expr MOD expr			+
            | expr GREATER expr     +
            | expr LESS expr		+
            | expr EQUAL expr		+
            | expr GREATEREQ expr	+
            | expr LESSEQ expr		+
            | expr NOTEQUAL expr    +
            | expr OR expr          +
            | expr AND expr         +
            | NOT expr               +
            | ADD expr				 +
            | SUB expr				 +
            | ID					 +
            | ID ASSIGN expr		 +
            | ID LPAREN clist RPAREN +
            | INT					 +
            | STRING                 +
    """

    if len(p) == 2:  # INT | STRING | ID
        p[0] = p[1]

    if len(p) == 3:  # | NOT expr | SUB expr | ADD expr
        if p[1] == t_SUB:
            p[0] = UnaryOpNode(
                p[1], p[2]
            )  # expression : SUB expression %prec UMINUS (unary minus operator has higher precedence than other operators in the expression)
        elif p[1] == t_NOT:
            p[0] = UnaryNotNode(p[1], p[2])  # expression : NOT expression %prec UNOT
        else:
            p[0] = p[2]

    if len(p) == 4:
        
        if p[1] == t_ASSIGN:  # ID ASSIGN expr  %prec ASSIGN
            p[0] = AssignNode(None, p[1], p[3])
            
        elif p[2] in (
            t_MOD,
            t_INTDIV,
            t_ADD,
            t_SUB,
            t_MULT,
            t_DIV,
            t_EXP,
        ):  # arethmatic
            p[0] = BinOpNode(p[2], p[1], p[3])
            
        elif p[2] in (t_AND,t_OR):
            p[0] = BoolOpNode(p[2],p[1],p[3])
            
         """clist : empty
              | exp
              | expr COMMA clist
        """
        elif p[1] == t_LBLOCK: # LBLOCK clist RBLOCK
            p[0] = ListNode(p[1])

        else:  # compare
            p[0] = CompNode(p[2], p[1], p[3])
            
            

    if len(p) == 5: # ID LPAREN clist RPAREN
        
        if p[1] == t_LPAREN:
            p[0] = FunctionCallNode(p[1], p[3])
        
        else: # expr LBLOCK expr RBLOCK %prec INDEX  *** also STRING LBLOCK expression RBLOCK  ***
            p[0] = IndexNode(p[1], p[3])
        
        
    if len(p) == 6: # expr QUESTIONMARK expr COLON expr
        p[0] = TernaryOperatorNode(p[1], p[3], p[5])



# self.name.evaluate(self.args.evaluate())
def p_clist(p):
    """clist : empty
              | exp
              | expr COMMA clist
    """

    if len(p) == 1:     # empty
        p[0] = []
        
    elif len(p) == 2:   # exp
        p[0] = p[1]
        # p[0] = [p[1]]
        
    else:               # expr COMMA clist
        p[0] = p[1]
        p[3].insert(0,p[1])
        p[0] = p[3]


# symbol_table[self.vnode.vid] = self.exp.evaluate()

# arg_dict = {arg.id: arg.evaluate() for arg in self.flist}


def p_flist(p):
    """flist : empty
              | ID COLON TYPE
              | ID COLON TYPE COMMA flist
    """
    if len(p) == 1: # empty
        p[0] = []
        
    elif len(p) == 6:  # ID COLON TYPE COMMA flist
        p[0] = p[1]
        p[5].insert(0, p[0])   # inserts it at the beginning of p[5]
        p[0] = p[5]
        
    else:            #  ID COLON TYPE
        p[0] = p[1]


def p_empty(p):
    "empty :"
    pass



# def p_statement_print(token):
#     "print_smt : PRINT LPAREN expression RPAREN SEMI %prec PRINT"
#     token[0] = PrintNode(token[3])


# def p_statment_assign_to_list(token):
#     """assign_to_list : ID LBLOCK expression RBLOCK ASSIGN expression SEMI %prec ASSIGN"""
#     token[0] = AssignToListNode(token[1], token[3], token[6])


# def p_statement_solo_block(token):
#     "solo_block : block"
#     token[0] = BlockNode(token[1])


# def p_expression_inlist(token):
#     """expression : expression IN expression %prec IN"""
#     token[0] = ContainsNode(token[3], token[1])


# def p_expression_group(token):
#     "expression : LPAREN expression RPAREN"
#     token[0] = token[2]



# def p_expression_exp(token):
#     """expression : expression EXP expression"""
#     token[0] = ExpNode(token[1], token[3])


def p_error(tok):

    if tok is None:
        # Handle unexpected end of input
        print("\nunexpected end of input")
    else:
        # Handle invalid token
        print(
            f"\nunexpected token ({tok.value}) at line {tok.lineno}, column {tok.lexpos - 2}"
        )

    raise SyntaxError


parser = yacc.yacc()
lexer = lex.lex()

f = open(sys.argv[1], mode="r")
data = f.read()

lexer.input(data)
for tok in lexer:
    print(tok.type, "		", tok.value)


try:
    ast = yacc.parse(data)
    ast.execute()
except SyntaxError:
    print("Syntax Error")
except Exception:
    print("Semantic Error")
