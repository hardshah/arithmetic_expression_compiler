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
    def p_expression(self):
        left_term = self.parse_term() #Keep parsed left term
        while self.current and self.current.type in ('PLUS', 'MINUS'):
            operation = self.current.type
            self.next_token()
            right_term = self.p_term()#Parsed right term
            left_term = ('operation', operation, left_term, right_term)
        
        return left_term
    
    ## term ::= factor "*" term
    ##        | factor "/" term
    ##        | factor
    def p_term(self):
        left_factor = self.p_factor() #Keep parsed left factor
        while self.current and self.current.type in ('DIVIDE', 'MULTIPLY'):
            operation = self.current.type
            self.next_token()
            right_factor = self.p_factor() # Parsed right factor
            left_factor = ('operation', operation, left_factor, right_factor) #Apply operation to both

        return left_factor
        
    ## factor ::= number
    ##          | identifier
    ##          | "(" expression ")"
    def p_factor(self):
        match self.current.type:
            case 'NUMBER':
                number = self.current.value
                self.next_token()
                return ('number', number)
            case 'IDENTIFIER':
                id = self.current.value
                self.next_token()
                return ('identifier', id)
            case 'LPAREN':
                self.next_token()
                expression = self.parse_expression()
                self.next_token()
                return expression

    
    ## assignment ::= identifier "=" expression
    def p_assignment():

    ## variable_declaration ::= "let" identifier "=" expression
    def p_variable_declaration():

    
    

    

    ## identifier ::= [a-zA-Z_][a-zA-Z0-9_]*
    def p_identifier():

    ## number ::= \d+
    def p_number():