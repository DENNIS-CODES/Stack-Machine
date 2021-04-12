# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 22:01:09 2021

@author: user
"""

"""
Program to create a Stack Machine to 
verify if an input string is a palendrome
i.e. abba but not aabb

"""

# Define Stack machine class
class StackMachine(object):
    """Represents a Stack machine."""
    SMRules = {}   # dictionary of SM rules
	
    def __init__(self):
        self.Stack = ['S']			# populate stack with initial 'S'
        self.size = 1				# set size of stack to 1
        self.SMRules = {}           # Place rules here
		
    def pop(self):
        if len(self.Stack) <1:
            pass
        else:
            self.Stack.pop(0)
            self.size-=	1			# reduce stack size by 1
        return

    def peek(self):
        ss = ""
        if len(self.Stack) < 1:
            return ""
        else:
            ss = self.Stack
            return ss[0]
 
    def stackIsEmpty(self):
        if len(self.Stack) == 0:
            return True
        else:
            return False
 
    def push(self,str):
        sStr = str[::-1] # slicing 
        for chr in sStr:
            self.Stack.insert(0,chr)	# push string onto top of stack
        self.size = len(self.Stack)
        return
		
    def printStack(self):
        print("Stack: [",end='')
        for item in self.Stack:
            print(item,end='')
        print("]")
        return
        
    def printRules(self):
        print("SM Rules:")
        rn = 1
        for key, value in self.SMRules.items():
            print("Rule",rn,"%4s" % key,"|", value) 
            rn += 1			
        return

    def printStep():
        """ Print out each step of the process """
        

				
def getInputString():
    """ get input to determine if it is a palindrome """
    
	
def processString(string,Stk):
    """ Process the input string to determine if it is a palindrome """
	
def main():
    """ You might have something like the following """
    pString = getInputString()
    Stk = StackMachine()
    processString(pString,Stk)
   
	
	
if __name__ == '__main__':
    main()
		

