import ply.lex as lex
import ply.yacc as yacc
import AstVistor
import MyParser
import Mylexer
import re


def has_main_function(input_string):
    pattern = r"def\s+\w+\s+main\s*\(\s*\)"
    return bool(re.search(pattern, input_string))
    # pattern = r"def\s+int\s+main\s*\(\s*int\s+\w+\s*,\s*int\s+\w+\s*\)\s*{\s*.*\s*}"


def reverse_procs(file_path):
    procs = {}
    proc_name = None
    with open(file_path) as f:
        lines = f.readlines()
        for line in reversed(lines):
            if line.startswith("proc "):
                proc_name = line.strip()
                procs[proc_name] = []
            else:
                procs[proc_name].append(line)

    with open(file_path, "w") as f:
        for proc_name in reversed(list(procs.keys())):
            f.write(proc_name + "\n")

            f.writelines(reversed(procs[proc_name]))
            f.write("\n")


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
        # try:
        parser.parse(lexer=lexer)
        # except Exception as e:
        # print(e)

        MyParser.parser = parser

    # Usage: Call the reverse_procs function with the path to the input file
    reverse_procs("IRtest.txt")
