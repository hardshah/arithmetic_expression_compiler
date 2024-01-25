from lexer import lexer
from recursive_descent_parser import Parser

INPUT_CODE = """
let x = 5 * ((2+3)/3);
id = x * 30 + 5
"""
def tokenize(input):
    lexer.input(input)
    return iter(lexer.token, None)

def main():
    lexer.input(INPUT_CODE)
    tokens = lexer.tokenize()
