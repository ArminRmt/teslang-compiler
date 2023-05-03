import Mylexer
from PraserAst import *
from Mylexer import find_column

# from ply.lex import LexTokens


# from main import parser

# from ParserAst import failing_rules


funcNames = ["scan", "print", "list", "length", "exit"]

# import some required globals from tokenizer
tokens = Mylexer.tokens
precedence = Mylexer.precedence


def p_prog(p):
    """
    prog : func prog
         | empty
    """

    if len(p) == 3:
        # print("p =", vars(p))
        p[0] = [p[1], p[2]]


def p_func(p):
    """func : DEF type ID LPAREN flist RPAREN LBRACE body RBRACE
    | DEF type ID LPAREN flist RPAREN RETURN expr SEMI
    """
    # breakpoint()
    p[0] = PraserAst(action="function", params=[p[2], p[3], p[5], p[8]]).execute()

    # if p[0] is None:
    #     failed_rules.append("p_func")
    if p[9] == ";":
        PraserAst(action="return_type", params=[p[8], p[2]]).execute()

    # p[0] = [p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]]


def p_body(p):
    """
    body : stmt body
         | empty
    """

    if len(p) == 3:
        p[0] = [p[1], p[2]]


def p_stmt(p):
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
        if p[1] == "return":
            # breakpoint()
            return_line = p.slice[1].lineno - 4
            # print(p.slice[1])
            PraserAst(
                action="return_type2", params=[p.stack, p[2], return_line]
            ).execute()


def p_if_statement(p):
    "if_statement : IF LPAREN expr RPAREN stmt"
    p[0] = PraserAst(action="condition", params=[p[3], p[5]]).execute()


def p_ifelse_statement(p):
    "ifelse_statement : IF LPAREN expr RPAREN stmt ELSE stmt"
    p[0] = PraserAst(action="condition", params=[p[3], p[5], p[7]]).execute()


def p_while_statement(p):
    "while_statement : WHILE LPAREN expr RPAREN stmt"
    p[0] = PraserAst(action="while", params=[p[3], p[5]]).execute()


def p_for_statement(p):
    "for_statement : FOR LPAREN ID ASSIGN expr TO expr RPAREN stmt"
    # p[0] = [p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]]
    p[0] = PraserAst(action="for", params=[p[3], p[5], p[7], p[9]]).execute()


def p_defvar(p):
    """
    defvar : VAR type ID
           | VAR type ID ASSIGN expr
    """

    if len(p) == 6:
        p[0] = PraserAst(action="declare_assign", params=[p[3], p[2], p[5]]).execute()
    else:
        p[0] = PraserAst(action="declare", params=[p[3], p[2]]).execute()


def p_flist(p):
    """
    flist :  type ID
          |  type ID COMMA flist
          | empty
    """

    if len(p) == 3:  #  TYPE ID
        p[0] = [(p[1], p[2])]
        # PraserAst(action="type_check", params=[p[1]]).execute()
        PraserAst(action="func_arguman", params=[p[2], p[1]]).execute()
        # PraserAst(action="type_cheak", params=[p[1]]).execute()

    elif len(p) == 5:  # TYPE ID COMMA flist
        p[0] = [(p[1], p[2])] + p[4]
        PraserAst(action="func_arguman", params=[p[2], p[1]]).execute()


# def p_flist_error(p):
#     """
#     flist : error ID
#     """
#     valid_types = ['str', 'int', 'null', 'vector']
#     print("grammer flist has error type should be in",valid_types)


def p_type(p):
    """
    type : INT
         | VECTOR
         | NULL
         | STRING
    """
    p[0] = p[1]

    # p[0] = PraserAst(action="type_check", params=[p[1]]).execute()


# def p_type_error(p):
#     """
#     type : error
#     """

#     for item in p.stack:
#         if isinstance(item, LexToken) and item.type == "ID":
#             function_name = item.value
#             break

#     print("\n↪ function", function_name)
#     print("↪ types must be one of the following 'int', 'string', 'vector', 'null'")


def p_expr(p):
    """expr : expr QUESTIONMARK expr COLON expr
    | ID LPAREN clist RPAREN
    | ID LBLOCK expr RBLOCK ASSIGN expr
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
    | builtin_methods
    """

    if len(p) == 2:  # INT | STRING | ID | builtin_methods
        p[0] = p[1]

    elif len(p) == 3:  # | NOT expr | SUB expr | ADD expr
        return_line = p.slice[1].lineno
        if p[1] == "-":
            p[0] = PraserAst(
                action="binop", params=[-1, "*", p[2], return_line]
            ).execute()
        elif p[1] == "+":
            p[0] = PraserAst(
                action="binop", params=[1, "*", p[2], return_line]
            ).execute()
        else:
            p[0] = PraserAst(action="UnaryNot", params=[p[2], return_line]).execute()

    elif len(p) == 4:
        if p[2] == "&&" or p[2] == "||":
            p[0] = PraserAst(action="logop", params=p[1:]).execute()
        elif p[2] == "=":  # ID ASSIGN expr
            return_line = p.slice[2].lineno - 4

            p[0] = PraserAst(
                action="assign", params=[p[1], p[3], p.stack, return_line]
            ).execute()
            # _______________________ type should be expr type   ______________________________________________________________
        elif p[1] == "[":  # LBLOCK clist RBLOCK    making list
            p[0] = PraserAst(action="ListNode", params=[p[2]]).execute()
        else:
            return_line = p.lineno(2) - 2
            p[0] = PraserAst(
                action="binop", params=p[1:], return_line=return_line
            ).execute()
            # PraserAst(action="binop2", params=[p[0], p[2], p.stack]).execute()

    elif len(p) == 5:
        if p[2] == "(":  # ID LPAREN clist RPAREN
            return_line = p.slice[1].lineno - 11
            PraserAst(action="FunctoinCall", params=[p[1], p[3], return_line]).execute()
            p[0] = [p[1], p[2], p[3], p[4]]
        else:  # expr LBLOCK expr RBLOCK           list index
            p[0] = PraserAst(action="ArrayIndex", params=[p[1], p[3]]).execute()

    elif len(p) == 6:  # expr QUESTIONMARK expr COLON expr
        p[0] = PraserAst(action="thearnaryOp", params=[p[1], p[3], p[5]]).execute()

    elif len(p) == 7:  # ID LBLOCK expr RBLOCK ASSIGN expr
        return_line = p.slice[2].lineno - 8
        # return_line = p.lineno(4)

        p[0] = PraserAst(
            action="list_assignment", params=[p[1], p[3], p[6], return_line]
        ).execute()


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

    # p[0] = [p[1]] if len(p) == 2 else [p[1]] + p[3] if len(p) == 4 else None


def p_empty(p):
    "empty :"
    p[0] = []


def p_builtin_methods(p):
    """
    builtin_methods : LENGTH LPAREN expr RPAREN
                    | SCAN LPAREN RPAREN
                    | PRINT LPAREN expr RPAREN
                    | LIST LPAREN expr RPAREN
                    | EXIT LPAREN expr RPAREN
    """
    if p[1] == "list":
        p[0] = PraserAst(action="builtin_list", params=[p[3]]).execute()

    # cases = {
    #     # "length": PraserAst(action="builtin_length", params=[p[3]]).execute(),
    #     # "scan": input(),
    #     # "print": PraserAst(action="print", params=[p[3]]).execute(),
    #     "list": PraserAst(action="builtin_list", params=[p[3]]).execute(),
    #     # "exit": sys.exit(int(p[3])),
    # }

    # p[0] = cases.get(p[1], None)  #  If the key is not found, None is returned.


# class SyntaxError():
#     def __init__(self, token):
#         self.token = token

#     def __str__(self):
#         return f"{self.message} at line {self.token.lineno}, position {self.token.lexpos}, near '{self.token.value}'"


def p_error(tok):
    if tok is None:
        # Handle unexpected end of input
        print("\nunexpected end of input")
    else:
        # Handle invalid token
        print(
            f"\nunexpected token ({tok.value}) at line {tok.lineno}, column {find_column(tok)}",
            end="",
        )


#     if failed_rules:
#         print("Failed rules:")
#     for rule in failed_rules:
#         print(f" - {rule}")
#     failing_rules = []  # Clear for next error
