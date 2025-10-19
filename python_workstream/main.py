class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b
    
    
