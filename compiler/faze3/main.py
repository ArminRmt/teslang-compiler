import ply.lex as lex
import ply.yacc as yacc
import MyParser
import Mylexer
import re


# teslang must have main funciton this sholuld not impliment on this file but it was hard for me to read my file in other classes
def has_main_function(input_string):
    pattern = r"def\s+\w+\s+main\s*\(\s*\)"
    return bool(re.search(pattern, input_string))


# this mehtod is created for showing intermidate code in a stucter that my task was to do it and i couldn't manage my time to do it in a better way so i did it in this way
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

        parser = yacc.yacc(module=MyParser)
        try:
            parser.parse(lexer=lexer)
        except Exception as e:
            print(e)

        MyParser.parser = parser

    reverse_procs("IRtest.txt")
