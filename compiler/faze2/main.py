import ply.lex as lex
import ply.yacc as yacc
import MyParser
import Mylexer
import re

from PraserAst import MyException

# from PraserAst import MyException2


# Build the lexer
lexer = lex.lex(module=Mylexer)

f = open("test.txt", "r")
data = f.read()
f.close()


###########   faze 1

lexer.input(data)
# for tok in lexer:
#     print(tok.type, "		", tok.value)


###########   faze 2

# Build the parser
parser = yacc.yacc(module=MyParser)
# parser.parse(lexer=lexer)


def find_position(followed_string, res):
    start_index = data.find(followed_string)

    # Add the length of the specific string to get the start position of the following string
    res_start_position = start_index + len(followed_string)

    res_index = data.find(res)

    line_number = data.count("\n", 0, res_index) + 1
    column_number = res_index - data.rfind("\n", 0, res_index)

    print(
        f"'{followed_string}' is line {line_number}, column {column_number + len(res)}."
    )


def find_var_position(var_name, followed_string):
    if followed_string == "return":
        var_regex = r"return\s+(\w+)\s*;"  # return A;
    elif followed_string == "=":
        # var_regex = (
        #     r"var\s+int\s+(\w+)\s*=\s*(\w+)\s*\+\s*(\d+)\s*;"  #     var int b = c + 1;
        # )
        var_regex = r"var\s+int\s+(\w+)\s*=\s*([-\w\s()+*/]*\d|[^\W\d_]+)\s*;"

    var_match = re.search(var_regex, data)
    if var_match:
        line_num = data.count("\n", 0, var_match.start()) + 1
        col_num = var_match.start() - data.rfind("\n", 0, var_match.start())
        return f"{var_name} is declared at line {line_num}, column {col_num}"
    else:
        return f"{var_name} is not declared in the code"


# try:
#     parser.parse(lexer=lexer)  # pass the lexer to the parse method
# except Exception as e:
#     if e is not None:
#         find_position(data, e.args[1], str(e.args[0]))
#     else:
#         print(f"{e.args[0].__class__.__name__}: {e.args[0]} at the end of file")


try:
    parser.parse(lexer=lexer)
except MyException as e:
    if e is not None:
        # find_position(e.followed_string, e.res)
        print(
            find_var_position(
                e.res,
                e.followed_string,
            )
        )

    else:
        print(f"Error: {e.message}")

# except MyException2 as e2:
#     if e2 is not None:
#         find_position(data, e2.followed_string, e2.res)
#     else:
#         print(f"Error: {e2.message}")

# exceptions = []

# try:
#     parser.parse(lexer=lexer)
# except Exception as e:
#     if isinstance(e, (MyException, MyException2)):
#         if e is not None:
#             # find_position(data, e.followed_string, e.res)
#             exceptions.append(find_position(data, e.followed_string, e.res))
#         else:
#             print(f"Error: {e.message}")
#     else:
#         print(f"Unhandled Exception: {e}")

# for e in exceptions:
#     print(e)
