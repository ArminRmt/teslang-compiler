import ply.lex as lex
from PraserAst import *

reserved = {
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "not": "NOT",
    "and": "AND",
    "or": "OR",
    # "in": "IN",
    "print": "PRINT",
    "var": "VAR",
    "def": "DEF",
    "for": "FOR",
    "to": "TO",
    "return": "RETURN",
    "null": "NULL",
    "str": "STRING",
    "vector": "VECTOR",
}

tokens = [
    "INT",
    "LPAREN",
    "RPAREN",
    "LBLOCK",
    "RBLOCK",
    # "BOOL",
    # "EXP",
    "MULT",
    "DIV",
    "MOD",
    # "INTDIV",
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
    # "COMMENT",
    "COMMA",
    "COLON",
    "QUESTIONMARK",
    "TYPE",
] + list(reserved.values())

# t_INT = r"\d+"
# t_TYPE = r"int|vector|str|null"
t_TO = r"to"
t_IF = r"if"
t_COMMA = r","
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBLOCK = r"\["
t_RBLOCK = r"\]"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_MOD = r"%"
# t_INTDIV = r"//"
t_ADD = r"\+"
t_SUB = r"\-"
t_MULT = r"\*"
t_DIV = r"\/"
# t_EXP = r"\*\*"
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
t_RETURN = r"return"


def t_TYPE(token):
    r"int|vector|str|null"
    token.value = TypeNode(token.value)
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


# def t_STRING(t):
#     r'"(?:\\"|.)*?"'

#     # hiqen thonjezat dhe karakteret e escape
#     t.value = bytes(t.value.lstrip('"').rstrip('"'), "utf-8").decode("unicode_escape")


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


# illegal character is encountered during lexical analysis
def t_error(token):
    print("Illegal character '%s'" % token.value[0])
    token.lexer.skip(1)


lexer = lex.lex()
