def visit(node, table):
    match node.type:
        case "var_declaration":
            return check_var_declaration(node, table)
        case "operation":
            return check_operation(node, table)
        case "assignment":
            return check_assignment(node, table)
        case "identifier":
            return check_identifier(node, table)
        case "number": #By definition
            return 'int'
        case _:
            raise Exception('Node type does not exist')

def check_var_declaration(node, table):
    type, name, expression  = node
    expression_type = visit(expression, table) #Check that expression type

    if expression_type == 'int':
        table.add(name, 'int') #add variable as an integer type
    else:
        raise TypeError('Type error in variable declaration')

def check_operation(node, table):
    type, operator, left, right = node
    left_type, right_type = visit(left, table), visit(right, table)

    if left_type == right_type: ## Check both operands are same type
        return left_type
    else:
        raise TypeError('Type error in operation')

def check_identifier(node, table):
    type, name = node 
    id_type = table.lookup(name) #Find identifier type
    if id_type:
        return id_type #return the type
    else:
        raise Exception('identifier has no type')

def check_assignment(node, table):
    type, name, expression = node
    expression_type = visit(expression, table) #Find expression type
    var_type = table.lookup(name)
    if var_type: 
        if var_type == expression_type: #Checking that variable type matches expression type
            return var_type
        else:
            raise TypeError('Cannot assign this expression type to this variable type')
    else:
        raise Exception('Variable has no type')