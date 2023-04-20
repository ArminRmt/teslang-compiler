from re import escape
from ply.lex import TOKEN


states = (("string", "inclusive"),)

# List of basic token names.
tokens = (
    # "INT",
    "SEMI",
    "ID",
    # "COMMENT",
    # "TYPE",
    "BUILTIN_METHODES",
    "SCAN",
    "LIST",
    "LENGTH",
    "EXIT",
)

reserved = {
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    # "in": "IN",
    "print": "PRINT",
    "scan": "SCAN",
    "length": "LENGTH",
    "exit": "EXIT",
    "var": "VAR",
    "def": "DEF",
    "for": "FOR",
    "to": "TO",
    "return": "RETURN",
    "null": "NULL",
    "str": "STRING",
    "int": "INT",
    "vector": "VECTOR",
}

# List of single character literals
specials_sc = {
    "+": "ADD",
    "-": "SUB",
    "*": "MULT",
    "/": "DIV",
    "%": "MOD",
    "=": "ASSIGN",
    "<": "LESS",
    ">": "GREATER",
    "{": "LBRACE",
    "}": "RBRACE",
    "(": "LPAREN",
    ")": "RPAREN",
    "[": "LBLOCK",
    "]": "RBLOCK",
    ",": "COMMA",
    ":": "COLON",
    "?": "QUESTIONMARK",
    "!": "NOT",
    # ";": "SEMI",
}


# List of multi character literals
specials_mc = {
    ">=": "GREATEREQ",
    "<=": "LESSEQ",
    "==": "EQUAL",
    "!=": "NOTEQUAL",
    "&&": "AND",
    "||": "OR",
    # "**": "POW",
}

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

tokens = (
    list(tokens)
    + list(reserved.values())
    + list(specials_mc.values())
    + list(specials_sc.values())
)
specials_sc_re = "[" + escape("".join(specials_sc.keys())) + "]"
specials_mc_re = "(" + "|".join(escape(x) for x in specials_mc.keys()) + ")"


# t_AND = r"\&\&"
# t_OR = r"\|\|"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")
    # t.lexer.lineno += len(t.value)


def find_column(token):
    last_cr = token.lexer.lexdata.rfind("\n", 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    return token.lexpos - last_cr


# def t_TYPE(t):
#     r"int|vector|str|null"
#     t.type = reserved.get(t.value.lower())
#     return t


# def t_BUILTIN_METHODES(t):
#     # r"scan|print|list|length|exit"
#     r"scan()|print([a-zA-Z_][a-zA-Z_0-9]*)|list()|length([a-zA-Z_][a-zA-Z_0-9])|exit(\d+)"
#     return t


def t_COMMENT(t):
    # r'(\\\\(.|\n)*?\\\\)'
    r"\#.*"
    # print(t.value + 'ignored')
    pass


def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    # Check for reserved words
    t.type = reserved.get(t.value.lower(), "ID")
    return t


# A regular expression rule with some action code
def t_INT(t):
    r"(0|[1-9]\d*)"
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_SEMI(t):
    r"\n+|;+"
    t.lexer.lineno += len(t.value)
    t.type = "SEMI"
    # t.value = ';'
    return t


# Match the first {. Enter ccode state.
def t_STRING(t):
    r"[\"\']"
    t.lexer.begin("string")
    t.lexer.str_start = t.lexer.lexpos
    t.lexer.str_marker = t.value


def t_string_chars(t):
    r'[^"\'\n]+'


def t_string_newline(t):
    r"\n+"
    print(
        "Incorrectly terminated string %s"
        % t.lexer.lexdata[t.lexer.str_start : t.lexer.lexpos - 1]
    )
    t.lexer.skip(1)


def t_string_end(t):
    r"[\"\']"

    if t.lexer.str_marker == t.value:
        t.type = "STRING"
        t.value = t.lexer.lexdata[t.lexer.str_start : t.lexer.lexpos - 1]
        t.lexer.begin("INITIAL")
        return t


@TOKEN(specials_mc_re)
def t_SPECIAL_MC(t):
    t.type = specials_mc.get(t.value, "SPECIAL")
    return t


@TOKEN(specials_sc_re)
def t_SPECIAL_SC(t):
    t.type = specials_sc.get(t.value, "SPECIAL")
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"
# t_ignore = " \t\r\n\f\v\\"


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
