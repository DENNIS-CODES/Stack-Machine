##############################################################
"""
#program to check balanced parentheses in an expression example:

#Parentheses are balanced, if all opening parentheses have their corresponding closing parentheses.

#Given an expression as input, we need to find out whether the parentheses are balanced or not.
#For example, "(x+y)*(z-2*(6))" is balanced, while "7-(3(2*9))4) (1" is not balanced.
#The problem can be solved using a stack.
"""
class Stack:
    def __init__(self):
        self.items = []  
  
    def is_empty(self):
        return self.items == []
  
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop(0)
    
    def stack(self):
        return self.items

def balanced(expression):
    s = Stack()
    for i in expression:
        if i == '(':
            s.push(i)
        if i == ')':
            if '(' in s.stack():
                s.pop()
            else:
                return False


    if not s.stack():
        return True
    else:
        return False
        
print(balanced(input()))

