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


## Building parser

parser = yacc.yacc()
