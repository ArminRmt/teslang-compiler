import ply.lex as lex
import ply.yacc as yacc
import MyParser
import Mylexer

# from MyParser import p_error
from PraserAst import PraserAst


# Build the lexer
lexer = lex.lex(module=Mylexer)

f = open("test.txt", "r")
data = f.read()
f.close()


# faze 1
lexer.input(data)
# for tok in lexer:
#     print(tok.type, "		", tok.value)


# Build the parser
parser = yacc.yacc(module=MyParser)
parser.parse()


# result = parser.parse(data, lexer=lexer)
# parser = yacc.yacc(start='type', errorlog=yacc.NullLogger(), debug=0)


# try:
#     result = parser.parse()
# except Exception as e:
#     p_error(e)


# import ply.yacc as yacc

# # Import your lexer and parser modules
# from Mylexer import tokens
# from MyParser import *

# # Read input code from file
# with open("test.txt", "r") as f:
#     data = f.read()

# # Build the lexer
# lexer = lex.lex(module=Mylexer)

# # Build the parser
# parser = yacc.yacc(module=MyParser)

# # Parse the input code
# result = parser.parse(data, lexer=lexer)
