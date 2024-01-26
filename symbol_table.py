class SymbolTable:
    def __init__(self): #Constructor
        self.symbols = {}
        self.parent = None

    def add(self, name, type): #Add symbol to current symbol table
            self.symbols[name] = type
    
    def lookup(self, name):
         if name in self.symbols: #Check if in current symbol table
              return self.symbols[name]
         if self.parent:
              return self.parent.lookup(name) #Check if in parent symbol table
         return None
    
    def within_scope(self): #Create a new symbol table and set this symbol table as parent
         scope = SymbolTable()
         scope.parent = self 

    def exit_scope(self):
         return self.parent #Go back to parent symbol table

