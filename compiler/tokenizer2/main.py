import ply.lex as lex
import ply.yacc as yacc
import MyParser
import Mylexer

from PraserAst import PraserAst


# Build the lexer
lexer = lex.lex(module=Mylexer)

# Build the parser
parser = yacc.yacc(module=MyParser)


f = open("test.txt", "r")
data = f.read()
# f.close()


# lexer.input(data)
# for tok in lexer:
#     print(tok.type, "		", tok.value)


try:
    for x in parser.parse(data):
        PraserAst.resolve(x)
except SyntaxError:
    # stack_state_str = ", ".join([s.state for s in parser.stack])
    # stack_rule_str = ", ".join([s.name for s in parser.symstack])
    # print(
    #     f"Syntax error\nState stack: {stack_state_str}. Rule stack: {stack_rule_str}."
    # )
    print("Syntax error")

except Exception:
    print("\nSemantic Error")
    print(f"({tok.value}) at line {tok.lineno}, column {tok.lexpos}")
