class Visitor:
    def __init__(self, symbol_table):
        self.table = symbol_table
    
    def visit(self, node):
        match node[0]:
            case "var_declaration":
                return self.check_var_declaration(node)
            case "operation":
                return self.check_operation(node)
            case "assignment":
                return self.check_assignment(node)
            case "identifier":
                return self.check_identifier(node)
            case "number": ## By definition
                return 'int'
            case _:
                raise Exception('Node type does not exist')

    def check_var_declaration(self, node):
        type, name, expression  = node
        expression_type = self.visit(expression) #Check that expression type

        if expression_type == 'int':
            self.table.add(name, 'int') ## Add variable as an integer type
        else:
            raise TypeError('Type error in variable declaration')

    def check_operation(self,node):
        type, operator, left, right = node
        left_type, right_type = self.visit(left), self.visit(right)
        
        if left_type == right_type: ## Check both operands are same type
            return left_type
        else:
            print(left_type, right_type)
            raise TypeError('Type error in operation')

    def check_identifier(self, node):
        type, name = node 
        id_type = self.table.lookup(name) #Find identifier type
        if id_type:
            return id_type #return the type
        else:
            raise NameError('Variable was not declared')

    def check_assignment(self, node):
        type, name, expression = node
        expression_type = self.visit(expression) #Find expression type
        var_type = self.table.lookup(name)
        if var_type: 
            if var_type == expression_type: #Checking that variable type matches expression type
                return var_type
            else:
                raise TypeError('Cannot assign this expression type to this variable type')
        else:
            raise Exception('Variable has no type')