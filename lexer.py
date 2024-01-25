import ply.lex as lex

# Types of tokens in Rust
# List of token names
tokens = [
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LET',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
]

#SYMBOLS FOR EACH TOKEN USED IN GRAMMAR RULES
t_PLUS = r'\+' #a
t_MINUS = r'-' #b
t_MULTIPLY = r'\*' #c
t_DIVIDE = r'/' #d
t_LET = r'let' #e
t_EQUALS = r'=' #f
t_LPAREN = r'\(' #g
t_RPAREN = r'\)' #h
t_SEMICOLON = r';' #i

## Special rokens
def t_IDENTIFIER(t): #j
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'IDENTIFIER'
    return t

def t_NUMBER(t): #
    r'\d+'
    t.value = int(t.value)
    return t

## Error
def t_error(t):
    print("Syntax Error", t.value[0])
    t.lexer.skip(1)

## want to ignore these chars
t_ignore = ' \t\r\n'

lexer = lex.lex()