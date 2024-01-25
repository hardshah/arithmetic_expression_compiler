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
         if name in self.symbols:
              return self.symbols
    
    def within_scope(self): #Create a new symbol table and set this symbol table as parent
         scope = SymbolTable()
         scope.parent = self 

    def exit_scope(self):
         return self.parent #Go back to parent symbol table

        
        
