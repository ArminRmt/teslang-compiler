import ply.lex as lex
import ply.yacc as yacc
import MyParser
import Mylexer
import re

# from MyParser import p_error


def has_main_function(input_string):
    pattern = r"def\s+\w+\s+main\s*\(\s*\)"
    return bool(re.search(pattern, input_string))


if __name__ == "__main__":
    with open("test.txt", "r") as f:
        input_string = f.read()

        if not has_main_function(input_string):
            print("\n### semantic error ###\n( Main ) function is not defined\n")

        lexer = lex.lex(module=Mylexer)
        lexer.input(input_string)

        #########   faze 1    ###########
        # for tok in lexer:
        #     print(tok.type, "		", tok.value)

        ###########   faze 2    ###########
        parser = yacc.yacc(module=MyParser)
        # parser.errok()
        try:
            parser.parse(lexer=lexer)
        except Exception as e:
            print(e)

        MyParser.parser = parser
