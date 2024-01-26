def check_operation_node(node, symbol_table):
    left_type = visit(node.left, symbol_table)
    right_type = visit(node.right, symbol_table)
    
    return left_type if left_type==right_type else raise TypeError("Type of operands does not match")
