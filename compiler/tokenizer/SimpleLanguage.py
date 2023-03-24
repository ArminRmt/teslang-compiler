import sys

from MyParser import *
from Mylexer import *


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
    print("\nSemantic Error")
    print(f"({tok.value}) at line {tok.lineno}, column {tok.lexpos}")
