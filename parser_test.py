from lexer import lexer
from recursive_descent_parser import Parser

INPUT_CODE = """
let x = 5 * ((2+3)/3);
id = x * 30 + 5
"""
def tokenize(input):
    lexer.input(input)
    return iter(lexer.token, None)

def parse(tokens):
    parser = Parser(tokens=tokens)
    return parser.p_program()

def main():
    tokens = tokenize(INPUT_CODE)
    
    print(tokens)
main()