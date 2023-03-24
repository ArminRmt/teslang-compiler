import ply.yacc as yacc
from Mylexer import *
from PraserAst import *


# ast = ast()

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
    # ("left", "UNOT"),
    (
        "left",
        "LESS",
        "LESSEQ",
        "EQUAL",
        "NOTEQUAL",
        "GREATER",
        "GREATEREQ",
    ),  # comparison operators same precedence
    # ("left", "IN"),
    ("left", "ADD", "SUB"),  # arithmetic operators same precedence
    # ("left", "INTDIV"),  # //
    # ("left", "UMINUS"),  # The unary minus operator, -.
    ("left", "MOD"),
    ("left", "MULT", "DIV"),
    # ("right", "EXP"),  # The exponentiation operator, **.
    ("left", "LBLOCK"),  # {
    ("left", "VECTOR"),
    # ("left", "INDEX"),
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
    """prog :
    | func prog"""

    if len(p) == 3:
        p[0] = p[2]
        p[0].s1.insert(0, p[1])
    else:
        p[0] = BlockNode([])
        p[0].s1 = []
    # print("--------------------", p[0], "-----------")


def p_func(p):
    """func : DEF TYPE ID LPAREN flist RPAREN LBRACE body RBRACE
    | DEF TYPE ID LPAREN flist RPAREN RETURN expr SEMI
    """

    # newFCheck(p[3])

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
    stmt :    expr SEMI
            | defvar SEMI
            | IF LPAREN expr RPAREN stmt
            | IF LPAREN expr RPAREN stmt ELSE stmt
            | WHILE LPAREN expr RPAREN stmt
            | FOR LPAREN ID EQUAL expr TO expr RPAREN stmt
            | RETURN expr SEMI
            | LBRACE body RBRACE
            | func
            | print_smt
    """

    if len(p) == 2:  # func
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

    if len(p) == 9:  # FOR LPAREN ID EQUAL expr TO expr RPAREN stmt
        p[0] = ForNode(p[3], p[5], p[7], p[9])


def p_defvar(p):
    """defvar : VAR TYPE ID
    | VAR TYPE ID ASSIGN expr
    """

    p[0] = AssignNode(p[2], p[3], p[5])


def p_expr(p):
    """expr : expr LBLOCK expr RBLOCK
    | LBLOCK clist RBLOCK
    | expr QUESTIONMARK expr COLON expr
    | expr ADD expr
    | expr SUB expr
    | expr MULT expr
    | expr DIV expr
    | expr MOD expr
    | expr GREATER expr
    | expr LESS expr
    | expr EQUAL expr
    | expr GREATEREQ expr
    | expr LESSEQ expr
    | expr NOTEQUAL expr
    | expr OR expr
    | expr AND expr
    | NOT expr
    | ADD expr
    | SUB expr
    | ID
    | ID ASSIGN expr
    | ID LPAREN clist RPAREN
    | INT
    | STRING
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
            t_ADD,
            t_SUB,
            t_MULT,
            t_DIV,
            t_EXP,
        ):  # arethmatic
            p[0] = BinOpNode(p[2], p[1], p[3])

        elif p[2] in (t_AND, t_OR):
            p[0] = BoolOpNode(p[2], p[1], p[3])

        elif p[1] == t_LBLOCK:  # LBLOCK clist RBLOCK
            p[0] = ListNode(p[1])

        else:  # compare
            p[0] = CompNode(p[2], p[1], p[3])

    if len(p) == 5:  # ID LPAREN clist RPAREN

        if p[1] == t_LPAREN:
            p[0] = FunctionCallNode(p[1], p[3])

        else:  # expr LBLOCK expr RBLOCK %prec INDEX  *** also STRING LBLOCK expression RBLOCK  ***
            p[0] = IndexNode(p[1], p[3])

    if len(p) == 6:  # expr QUESTIONMARK expr COLON expr
        p[0] = TernaryOperatorNode(p[1], p[3], p[5])


# self.name.evaluate(self.args.evaluate())
def p_clist(p):
    """clist :
    | expr
    | expr COMMA clist
    """

    if len(p) == 1:  # empty
        p[0] = []

    elif len(p) == 2:  # exp
        p[0] = p[1]
        # p[0] = [p[1]]

    else:  # expr COMMA clist
        p[0] = p[1]
        p[3].insert(0, p[1])
        p[0] = p[3]


# symbol_table[self.vnode.vid] = self.exp.evaluate()

# arg_dict = {arg.id: arg.evaluate() for arg in self.flist}


def p_flist(p):
    """flist :
    | TYPE ID
    | TYPE ID COMMA flist
    """
    if len(p) == 1:  # empty
        p[0] = []

    elif len(p) == 5:  # TYPE ID COMMA flist
        p[0] = p[4]
        p[0].insert(0, [p[1], p[2]])  # inserts it at the beginning of p[0]

    else:  #  TYPE ID
        p[0] = [p[1], p[2]]


def p_type(p):
    """type : INT
    | VECTOR
    | NULL
    | STRING
    """
    p[0] = p[1]


def p_statement_print(p):
    "print_smt : PRINT LPAREN expr RPAREN SEMI %prec PRINT"
    p[0] = PrintNode(p[3])


# def p_empty(p):
#     "empty :"
#     pass


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
            f"\nunexpected token ({tok.value}) at line {tok.lineno}, column {tok.lexpos}"
        )

    raise SyntaxError


parser = yacc.yacc()
