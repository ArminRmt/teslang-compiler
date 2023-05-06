import ply.lex as lex
import ply.yacc as yacc
import MyParser
import Mylexer


if __name__ == "__main__":
    with open("test.txt", "r") as f:
        lexer = lex.lex(module=Mylexer)
        lexer.input(f.read())

        ###########   faze 1    ###########
        # # for tok in lexer:
        # #     print(tok.type, "		", tok.value)

        ###########   faze 2    ###########
        parser = yacc.yacc(module=MyParser)
        try:
            parser.parse(lexer=lexer)
        except Exception as e:
            print(e)
