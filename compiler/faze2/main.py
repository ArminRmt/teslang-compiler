import ply.lex as lex
import ply.yacc as yacc
import MyParser
import Mylexer

# from PraserAst import MyException
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
parser.parse(lexer=lexer)


# def find_position(followed_string, res):
#     start_index = data.find(followed_string)

#     # Add the length of the specific string to get the start position of the following string
#     res_start_position = start_index + len(followed_string)

#     res_index = data.find(res)

#     line_number = data.count("\n", 0, res_index) + 1
#     column_number = res_index - data.rfind("\n", 0, res_index)

#     print(f"The position of '{res}' is line {line_number}, column {column_number - 1}.")


# try:
#     parser.parse(lexer=lexer)  # pass the lexer to the parse method
# except Exception as e:
#     if e is not None:
#         find_position(data, e.args[1], str(e.args[0]))
#     else:
#         print(f"{e.args[0].__class__.__name__}: {e.args[0]} at the end of file")


# try:
#     parser.parse(lexer=lexer)
# except MyException as e:
#     if e is not None:
#         find_position(data, e.followed_string, e.res)
#     else:
#         print(f"Error: {e.message}")

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
