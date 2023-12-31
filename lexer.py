import ply.lex as lex

# Types of tokens in Rust
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

# Regular expression rules for simple tokens (Copied over from PLY docs example)
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

## want to ignore these chars
t_ignore = ' \t'

## Rules
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'IDENTIFIER'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

## Error handling
def t_error(t):
    print("Syntax Error", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()