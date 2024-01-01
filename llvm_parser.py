from llvmlite import ir, binding
import ply.yacc as yacc
from lexer import tokens

MODULE_NAME = "test"

# LLVM

binding.initialize()
binding.initialize_native_target()
binding.initialize_all_asmprinters()

## Creating Module

module = ir.Module(name = MODULE_NAME)
builder = ir.IRBuilder()

## AST Node Classes
class VariableDeclarationNode:
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

class AssignmentNode:
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value
 
#Grammar rules using bottom up parsing. Look-Ahead Left-to-Right Rightmost derivation


def p_program(p): ## Program is list of statements
    p[0] = p[1] ## program -> statements


## Building parser

parser = yacc.yacc()
