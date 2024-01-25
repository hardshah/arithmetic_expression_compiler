class Symbol:
    def __init__(self, name, type = None):
        self.name = name
        self.type = type
class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.parent = None

    
    def add(self, symbol):
            self.symbols[symbol.name] = symbol
    
    def lookup(self, name):
    
        
    def within_scope(self):

    def exit_scope(self):

        
        
