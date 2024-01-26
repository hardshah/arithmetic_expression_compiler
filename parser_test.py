from lexer import lexer
from recursive_descent_parser import Parser

INPUT_CODE = """
let x = 5 * ((2+3)/3);
id = x * 30 + 5;
"""
def tokenize(input):
    lexer.input(input)
    return iter(lexer.token, None)

def parse(tokens):
    parser = Parser(tokens=tokens)
    return parser.p_program()

def visualize_ast(node, indent=0):
    if node is None:
        return

    space = '  ' * indent

    if isinstance(node, tuple):
        print(f"{space}{node[0]}")
        for child in node[1:]:
            visualize_ast(child, indent + 1)
    elif isinstance(node, list):
        for statement in node:
            visualize_ast(statement, indent)
    else:
        print(f"{space}{node}")


def main():
    tokens = tokenize(INPUT_CODE)
    abstract_syntax_tree = parse(tokens)

    visualize_ast(abstract_syntax_tree)
    print(abstract_syntax_tree)
main()