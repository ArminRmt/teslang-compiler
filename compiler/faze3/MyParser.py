import Mylexer
from AstVistor import *
from Mylexer import find_column
import sys


tokens = Mylexer.tokens
precedence = Mylexer.precedence


def p_prog(p):
    """
    prog : func prog
    | empty
    """

    if len(p) == 3:
        p_func, p_prog = p[1], p[2]
        p[0] = [p_func, p_prog]


def p_func(p):
    """func : DEF type ID LPAREN flist RPAREN LBRACE body RBRACE
    | DEF type ID LPAREN flist RPAREN RETURN expr SEMI
    """

    f_type, f_name, f_args, f_body = p[2], p[3], p[5], p[8]

    p[0] = AstVistor(
        action="function", params=[f_type, f_name, f_args, f_body]
    ).execute()

    if p[9] == ";":
        AstVistor(action="return_type", params=[f_body, f_type]).execute()


def p_body(p):
    """
    body : stmt body
         | empty
    """

    if len(p) == 3:
        p_stmt, p_body = p[1], p[2]
        p[0] = [p_stmt, p_body]


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

    elif len(p) == 3:  # expr SEMI | defvar SEMI
        p[0] = p[1]

    elif len(p) == 4:  #  RETURN expr SEMI | LBRACE body RBRACE
        p_stack, p_expr, return_line = p.stack, p[2], p.slice[1].lineno - 4
        if p[1] == "return":
            AstVistor(
                action="return_type2", params=[p_stack, p_expr, return_line]
            ).execute()

        p[0] = p_expr


def p_if_statement(p):
    "if_statement : IF LPAREN expr RPAREN stmt"
    p_cond, p_stmt = p[3], p[5]
    p[0] = AstVistor(action="condition", params=[p_cond, p_stmt]).execute()


def p_ifelse_statement(p):
    "ifelse_statement : IF LPAREN expr RPAREN stmt ELSE stmt"
    p_cond, p_stmt, p_else_stmt = p[3], p[5], p[7]
    p[0] = AstVistor(action="condition", params=[p_cond, p_stmt, p_else_stmt]).execute()


def p_while_statement(p):
    "while_statement : WHILE LPAREN expr RPAREN stmt"
    p_cond, p_stmt = p[3], p[5]
    p[0] = AstVistor(action="while", params=[p_cond, p_stmt]).execute()


def p_for_statement(p):
    "for_statement : FOR LPAREN ID ASSIGN expr TO expr RPAREN stmt"
    # "for_statement : FOR LPAREN ID ASSIGN expr TO expr RPAREN LBRACE body RBRACE"

    loop_variable_name, loop_start, loop_end, loop_body = p[3], p[5], p[7], p[9]
    p[0] = AstVistor(
        action="for", params=[loop_variable_name, loop_start, loop_end, loop_body]
    ).execute()


def p_defvar(p):
    """
    defvar : VAR type ID
           | VAR type ID ASSIGN expr
    """

    p_type, p_name = p[2], p[3]

    if len(p) == 6:
        p_expr = p[5]
        p[0] = AstVistor(
            action="declare_assign", params=[p_name, p_type, p_expr, p.stack]
        ).execute()
    else:
        p[0] = AstVistor(action="declare", params=[p_name, p_type]).execute()


def p_defvar_error(p):
    """
    defvar : VAR error ID
           | VAR error ID ASSIGN expr
    """
    print(
        f"\n### Syntax error ###\nUnknown type '{p[2].value}' for variable ( {p[3]} )\n"
    )


def p_flist(p):
    """
    flist : type ID
          | type ID COMMA flist
          | empty
    """

    if len(p) == 3:  #  TYPE ID
        p[0] = [(p[1], p[2])]
        AstVistor(action="func_arguman", params=[p[2], p[1]]).execute()
        # AstVistor(action="type_cheak", params=[p[1]]).execute()

    elif len(p) == 5:  # TYPE ID COMMA flist
        p[0] = [(p[1], p[2])] + p[4]
        AstVistor(action="func_arguman", params=[p[2], p[1]]).execute()


def p_type(p):
    """
    type : INT
         | VECTOR
         | NULL
         | STRING
    """
    p[0] = p[1]


def p_expr(p):
    """expr : expr QUESTIONMARK expr COLON expr
    | ID LPAREN clist RPAREN
    | ID LBLOCK expr RBLOCK ASSIGN expr
    | ID LBLOCK expr RBLOCK
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

    if len(p) == 2:  # INT | STRING | ID | VECTOR | builtin_methods
        p[0] = p[1]

    elif len(p) == 3:  # | NOT expr | SUB expr | ADD expr
        p_expr, return_line = p[2], p.slice[1].lineno

        if p[1] == "-":
            p[0] = AstVistor(
                action="binop", params=[-1, "*", p_expr, return_line], stack=p.stack
            ).execute()
        elif p[1] == "+":
            p[0] = AstVistor(
                action="binop", params=[1, "*", p_expr, return_line], stack=p.stack
            ).execute()
        else:
            p[0] = AstVistor(action="UnaryNot", params=[p_expr, return_line]).execute()

    elif len(p) == 4:
        if p[2] == "&&" or p[2] == "||":
            p[0] = AstVistor(action="logop", params=p[1:]).execute()
        elif p[2] == "=":  # ID ASSIGN expr
            p_id, p_expr, return_line = p[1], p[3], p.slice[2].lineno - 5
            p[0] = AstVistor(
                action="assign", params=[p_id, p_expr, p.stack, return_line]
            ).execute()
            # TODO type should be expr type
        elif p[1] == "[":  # LBLOCK clist RBLOCK    making list
            p[0] = AstVistor(action="ListNode", params=[p[2]]).execute()
        else:
            return_line = p.lineno(2) - 2

            p[0] = AstVistor(
                action="binop", params=p[1:], return_line=return_line, stack=p.stack
            ).execute()

    elif len(p) == 5:
        if p[2] == "(":  # ID LPAREN clist RPAREN
            p_id, p_clist, return_line = p[1], p[3], p.slice[1].lineno - 11

            p[0] = AstVistor(
                action="FunctionCall", params=[p_id, p_clist, return_line]
            ).execute()
            # p[0] = [p[i] for i in range(1, 5)]

        else:  # ID LBLOCK expr RBLOCK            list index
            p_array, p_index, return_line = p[1], p[3], p.slice[1].lineno - 11
            p[0] = AstVistor(
                action="ArrayIndex", params=[p_array, p_index, return_line]
            ).execute()

    elif len(p) == 6:  # expr QUESTIONMARK expr COLON expr
        p_cond, p_expr, p_else_expr = p[1], p[3], p[5]

        p[0] = AstVistor(
            action="thearnaryOp", params=[p_cond, p_expr, p_else_expr]
        ).execute()

    elif len(p) == 7:  # ID LBLOCK expr RBLOCK ASSIGN expr
        p_array, p_index, p_expr, return_line = p[1], p[3], p[6], p.slice[2].lineno - 8
        p[0] = AstVistor(
            action="list_assignment", params=[p_array, p_index, p_expr, return_line]
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
        p[0] = AstVistor(action="builtin_list", params=[p[3]]).execute()
    elif p[1] == "print":
        p_stack = p.stack
        p[0] = AstVistor(action="print", params=[p[3], p_stack]).execute()
    elif p[1] == "length":
        array = p[3]
        p[0] = AstVistor(action="builtin_length", params=[array]).execute()
    elif p[1] == "scan":
        p[0] = AstVistor(action="builtin_scan").execute()

    elif p[1] == "exit":
        return_code = p[3]
        print("system exit code: " + str(return_code))
        sys.exit(return_code)


def p_error(tok):
    if tok is None:
        # Handle unexpected end of input
        print("\nunexpected end of input")
    else:
        # Handle invalid token
        print(
            f"\nunexpected token ({tok.value}) at line {tok.lineno}, column {find_column(tok)}",
            end="\n\n",
        )
