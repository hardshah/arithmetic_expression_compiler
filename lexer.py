import ply.lex as lex

# Types of tokens in Rust
# List of token names
tokens = [
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LET',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
]

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LET = r'let'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'

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

## want to ignore these chars
t_ignore = ' \t\r\n'

lexer = lex.lex()