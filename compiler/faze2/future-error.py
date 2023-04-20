import ply.yacc as yacc

# define your grammar rules here

# define the parser
def parse(input_string, start_rule):
    parser = yacc.yacc()
    return parser.parse(input_string, start=start_rule)

# define custom exception classes for each type of error
class SyntaxError(Exception):
    def __init__(self, message, lineno, column, rule):
        super().__init__(message)
        self.lineno = lineno
        self.column = column
        self.rule = rule

class SemanticError(Exception):
    def __init__(self, message, lineno, column, rule):
        super().__init__(message)
        self.lineno = lineno
        self.column = column
        self.rule = rule

# define the p_error method
def p_error(p):
    if p:
        # syntax error
        raise SyntaxError(
            f"Syntax error at token {p.type}, line {p.lineno}, column {p.lexpos}",
            p.lineno,
            p.lexpos - p.lexer.lineno,
            p.parser.rule
        )
    else:
        # unexpected end of input
        raise SyntaxError(
            "Unexpected end of input",
            p.lexer.lineno,
            p.lexer.lexpos - p.lexer.lineno,
            p.parser.rule
        )

# define a custom lexer with error handling
class Lexer:
    def __init__(self):
        self.lexer = ply.lex.lex()
    
    def input(self, text):
        self.lexer.input(text)
    
    def token(self):
        try:
            return self.lexer.token()
        except ply.lex.LexError as e:
            raise SemanticError(str(e), e.lineno, e.lexpos - e.lineno, "lexer")
    
    def __iter__(self):
        while True:
            token = self.token()
            if not token:
                break
            yield token

# call the parse function with the start rule and error handling
input_string = "..."
lexer = Lexer()
lexer.input(input_string)

try:
    result = parse(input_string, "my_start_rule")
except SyntaxError as e:
    print(f"Syntax error in {e.rule}: {e.msg} at line {e.lineno}, column {e.column}")
except SemanticError as e:
    print(f"Semantic error in {e.rule}: {e.msg} at line {e.lineno}, column {e.column}")
except Exception as e:
    print(f"Unknown error: {str(e)}")
