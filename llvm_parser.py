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
 
#Grammar rules using recursive descent parsing

## program : statement_list
def p_program(p):
    p[0] = p[1] 

##statement_list : statement SEMICOLON statement_list
##               | statement SEMICOLON  
def p_statement_list():

## statement ::= variable_declaration
##             | assignment
##             | expression
def p_statement():

## <expression> ::= term "+" expression
##                | term "-" expression
##                | term
def p_expression():
    
## assignment ::= identifier "=" expression
def p_assignment():

## variable_declaration ::= "let" identifier "=" expression
def p_variable_declaration():

## term ::= factor "*" term
##        | factor "/" term
##        | factor
def p_term():

## factor ::= number
##          | identifier
##          | "(" expression ")"
def p_factor():

## identifier ::= [a-zA-Z_][a-zA-Z0-9_]*
def p_identifier():

## number ::= \d+
def p_number():

## Building parser
parser = yacc.yacc()
