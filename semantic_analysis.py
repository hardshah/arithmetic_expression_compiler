def visit(node, table):
    match node[0]:
        case "var_declaration":
            return check_var_declaration(node, table)
        case "operation":
        
        case "assignment":
        
        case "number":
        
        case "identifier":
        
        case _:
            raise Exception('Node type does not exist')

def check_var_declaration(node, table):
    type, name, expression  = node
    expression_type = visit(expression, table)

    if expression_type == 'integer':
        table.add(name, 'int')

def check_operation(node, table):
    type, operator, left, right = node
    left_type, right_type = visit(left, table), visit(right, table)

    if left_type == right_type:
        return 'int'
    else:
        raise TypeError('Type error')