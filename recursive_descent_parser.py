

class Parser:
    def __init__(self, tokens): #Constructor
        self.tokens = tokens
        self.current =  None
        self.next_token()
    
    def next_token(self): #set current token to the next token
        self.current= next(self.tokens, None)
    ## program ::= statement_list
    def p_program(self):
        return self.p_statement_list()

    ##statement_list ::= statement SEMICOLON statement_list
    ##                 | statement SEMICOLON  
    def p_statement_list(self):
        statements = []
        while self.current is not None:
            statements.append(self.p_statement())
            if self.current.type == 'SEMICOLON': 
                self.next_token() ##Consume the semicolon
        return statements

    ## statement ::= variable_declaration
    ##             | assignment
    ##             | expression
    def p_statement(self):
        match self.current_token.type:
            case 'LET':
                return self.p_variable_declaration()
            case 'IDENTIFIER':
                return self.p_assignment()
            case _:
                return self.p_expression()

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