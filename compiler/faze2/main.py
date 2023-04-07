import ply.lex as lex
import ply.yacc as yacc
import MyParser
import Mylexer

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
parser = yacc.yacc(module=MyParser, debug=True)
parser.parse(tracking=True)
