import Mylexer
import sys
from PraserAst import PraserAst


funcNames = ["scan", "print", "list", "length", "exit"]

# function with the same name has already been defined
def newFCheck(t):
    if t in funcNames:
        print("function", t, "already exist!")
        raise Exception
    else:
        funcNames.append(t)


# import some required globals from tokenizer
tokens = Mylexer.tokens
precedence = Mylexer.precedence
astList = []


def p_prog(p):
    """
    prog : func prog
         | empty
    """

    if len(p) == 3:
        p[0] = [p[1], p[2]]


def p_func(p):
    """func : DEF TYPE ID LPAREN flist RPAREN LBRACE body RBRACE
    | DEF TYPE ID LPAREN flist RPAREN RETURN expr SEMI
    """
    # newFCheck(p[3])

    p[0] = PraserAst(action="function", params=[p[2], p[3], p[5], p[8]])


def p_body(p):
    """
    body : stmt body
         | empty
    """

    if len(p) == 3:
        p[0] = [p[1], p[2]]


def p_smt(p):

    """
    stmt :    expr SEMI
            | defvar SEMI
            | if_statement
            | ifelse_statement
            | while_statement
            | for_statement
            | RETURN expr SEMI
            | LBRACE body RBRACE
            | func
    """

    if (
        len(p) == 2
    ):  # func | if_statement | ifelse_statement | while_statement | for_statement
        p[0] = p[1]

    if len(p) == 3:  # expr SEMI | defvar SEMI
        p[0] = p[1]

    if len(p) == 4:  #  RETURN expr SEMI | LBRACE body RBRACE
        p[0] = p[2]


def p_if_statement(p):
    "if_statement : IF LPAREN expr RPAREN stmt"
    p[0] = PraserAst(action="condition", params=[p[3], p[5]])


def p_ifelse_statement(p):
    "if_statement : IF LPAREN expr RPAREN stmt ELSE stmt"
    p[0] = PraserAst(action="condition", params=[p[3], p[5], p[7]])


def p_while_statement(p):
    "while_statement : WHILE LPAREN expr RPAREN stmt"
    p[0] = PraserAst(action="while", params=[p[3], p[5]])


def p_for_statement(p):
    "for_statement : FOR LPAREN ID EQUAL expr TO expr RPAREN stmt"
    p[0] = PraserAst(action="for", params=[p[3], p[5], p[7], p[9]])


def p_defvar(p):
    """defvar : VAR TYPE ID
    | VAR TYPE ID ASSIGN expr
    """
    if len(p) == 6:
        p[0] = PraserAst(action="assign", params=[p[3], p[2], p[5]])
    else:
        p[0] = PraserAst(action="assign", params=[p[3], p[2]])


def p_flist(p):
    """
    flist : TYPE ID
          | TYPE ID COMMA flist
          | empty
    """
    if len(p) == 3:  #  TYPE ID
        p[0] = [[p[1], p[2]]]
        PraserAst(action="arguman_assign", params=[p[2], p[1]])

    elif len(p) == 5:  # TYPE ID COMMA flist
        p[0] = [[p[1], p[2]]] + p[4]
        PraserAst(action="arguman_assign ", params=[p[2], p[1], p[4]])


def p_expr(p):
    """expr : expr QUESTIONMARK expr COLON expr
    | ID LPAREN clist RPAREN
    | expr LBLOCK expr RBLOCK
    | LBLOCK clist RBLOCK
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
    | ID ASSIGN expr
    | NOT expr
    | ADD expr
    | SUB expr
    | ID
    | INT
    | STRING
    | builtin_scan
    | builtin_print
    | builtin_list
    | builtin_length
    | builtin_exit
    """

    if len(p) == 2:  # INT | STRING | ID | builtin_methods
        p[0] = p[1]
        p[0] = PraserAst(action="assign", params=[p[1], p[1].type])

    if len(p) == 3:  # | NOT expr | SUB expr | ADD expr
        if p[0] == "-":
            p[0] = PraserAst(action="binop", params=[-1, "*", p[2]])
        elif p[0] == "!":
            p[0] = PraserAst(action="UnaryNot", params=[p[2]])
        else:
            p[0] = p[1]

    if len(p) == 4:
        if p[2] == "&&" or p[2] == "||":
            p[0] = mAST(action="logop", params=p[1:])
        elif p[2] == "=":  # ID ASSIGN expr
            p[0] = PraserAst(action="assign", params=[p[1], p.type, p[3]])
        elif p[1] == "=":  # LBLOCK clist RBLOCK
            p[0] = PraserAst(action="ListNode", params=[p[2]])
        else:
            p[0] = PraserAst(action="binop", params=p[1:])

    if len(p) == 5:
        if p[2] == "(":  # ID LPAREN clist RPAREN
            pass
        else:  # expr LBLOCK expr RBLOCK
            pass

    if len(p) == 6:  # expr QUESTIONMARK expr COLON expr
        pass


def p_clist(p):
    """
    clist : expr
          | expr COMMA clist
          | empty
    """

    if len(p) == 2:  # expr
        p[0] = [p[1]]
    elif len(p) == 4:  # expr COMMA clist
        p[0] = [p[1]] + p[3]


# def p_flist(p):
#     """
#     flist : TYPE ID
#           | TYPE ID COMMA flist
#           | empty
#     """
#     if len(p) == 3:  #  TYPE ID
#         p[0] = [[p[1], p[2]]]
#         PraserAst(action="arguman_assign", params=[p[2], p[1]])

#     elif len(p) == 5:  # TYPE ID COMMA flist
#         p[0] = [[p[1], p[2]]] + p[4]
#         PraserAst(action="arguman_assign ", params=[p[2], p[1], p[4]])


# symbol_table[self.vnode.vid] = self.exp.evaluate()

# arg_dict = {arg.id: arg.evaluate() for arg in self.flist}


def p_type(p):
    """type : INT
    | VECTOR
    | NULL
    | STRING
    """
    p[0] = p[1]


def p_empty(p):
    "empty :"
    if len(p) == 1:  # prog
        print("last grammer empty prog")
    p[0] = []


def p_builtin_length(p):
    "expression : LENGTH LPAREN expr RPAREN"
    p[0] = len(p[3])


def p_builtin_scan(p):
    """builtin_scan : SCAN LPAREN RPAREN"""
    p[0] = input()


def p_builtin_print(p):
    """builtin_print : PRINT LPAREN expr RPAREN"""
    print(p[3])


def p_builtin_list(p):  # return list with n element
    """builtin_list : LPAREN expr RPAREN"""
    p[0] = list(range(int(p[2])))


def p_builtin_exit(p):
    """builtin_exit : EXIT LPAREN expr RPAREN"""
    sys.exit(int(p[3]))


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
