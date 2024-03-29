from compiler_components.lexer import lexer
from compiler_components.recursive_descent_parser import Parser
from compiler_components.symbol_table import SymbolTable
from compiler_components.visitor import Visitor
from compiler_components.intermediate_representation_generator import IRGenerator

INPUT_CODE = """
let x = 5 * ((2+3)/3);
x = (x * 30) + 5;
"""
def tokenize(input):
    lexer.input(input)
    return iter(lexer.token, None)

def compile(tokens):

    symbol_table = SymbolTable()
    parser = Parser(tokens, symbol_table)
    ast = parser.p_program()

    visitor = Visitor(symbol_table) #Perform checks
    for statement in ast:
        visitor.visit(statement)
    
    symbol_table = SymbolTable()
    ir_generator = IRGenerator(symbol_table)
    
    ir_generator.generate(ast)
    
    return ir_generator.module

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
    ir = compile(tokens)
    print(ir)


main()