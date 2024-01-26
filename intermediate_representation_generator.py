from llvmlite import ir
from visitor import Visitor

class IRGenerator(Visitor): ##inherit from visitor class
    def __init__(self, table):
        self.module = ir.Module()
        self.builder = None
        self.context = ir.Context()
        self.table = table
    
    def generate(self, ast):
        function_type = ir.FunctionType(ir.VoidType(), [])
        main_function = ir.Function(self.module, function_type, name = 'main')
        
        block = main_function.append_basic_block(name='entry')
        self.builder = ir.IRBuilder(block)

        for node in ast:
            self.visit(node)

        self.builder.ret_void()
        return str(self.module)
    
    def visit(self, node): # Override the visit function
        match node[0]:
            case 'var_declaration':
                return self.visit_var_declaration(node)
            case 'operation':
                return self.visit_operation(node)
            case 'assignment':
                return self.visit_assignment(node)
            case 'identifier':
                return self.visit_identifier(node)
            case 'number': ## By definition
                return self.visit_number(node)
            case _:
                raise Exception('Node type does not exist')

    
    def visit_var_declaration(self, node):
        type, name, expression = node
        value = self.visit(expression)
        alloc = self.builder.alloca(ir.IntType(32), name = name)
        self.builder.store(value, alloc)
        self.table.add(name, alloc)

    def visit_assignment(self, node):
        type, name, expression = node
        value = self.visit(expression)
        alloc = self.table.lookup(name)
        if alloc is not None:
            self.builder.store(value, alloc)
        else:
            raise ValueError(f"Variable is not declared.")
    
    def visit_operation(self, node):
        type, operation, left, right = node
        left_val, right_val = self.visit(left), self.visit(right)
        match operation:
            case 'PLUS':
                return self.builder.add(left_val, right_val)
            case 'MINUS':
                return self.builder.sub(left_val, right_val)
            case 'MULTIPLY':
                return self.builder.mul(left_val, right_val)
            case 'DIVIDE':
                return self.builder.sdiv(left_val, right_val)
            case _:
                raise ValueError(f"Encountered unsupported operation")

    def visit_number(self, node):
        type, num = node
        return ir.Constant(ir.IntType(32), num)

    def visit_identifier(self, node):
        type, name = node
        alloc = self.table.lookup(name)
        if alloc is not None:
            return self.builder.load(alloc, name)
        else:
            raise ValueError(f"Variable was not declared.")