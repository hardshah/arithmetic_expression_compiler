import ply.lex as lex

# Types of tokens
tokens = [
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LET',
    'EQUALS',
    'SEMICOLON',
]

lexer = lex.lex()