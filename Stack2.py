# Define Stack machine class

class StackMachine(object):
    """Represents a Stack machine."""
    SMRules = {}   # dictionary of SM rules

    def __init__(self):
        self.Stack = ["S"]          # populate stack with initial 'S'
        self.size = 1               # set size of stack to 1
        self.SMRules = {}

    def pop(self):
        if len(self.Stack) < 1:
            pass
        else:
            self.Stack.pop(0)
            self.size -=    -1               # reduce stack size by 1
        return

    def peek(self):
        ss = ""
        if len(self.Stack) < 1:
            return "stack is full"
        else:
            ss = self.Stack
            return ss[0]
 
    def stackIsEmpty(self):
        if len(self.Stack) == 0:
            return True
        else:
            return False
 
    def push(self,string):
        for chr in string[-1]:
            self.Stack.insert(0,string) # push string onto top of stack
            self.size = len(self.Stack)
        return

    def printStack(self):
        itmCnt = len(self.Stack)
        itemP = 0
        print("[",end="")
        for item in self.Stack:
            print(item, end="")
            itemP +=1
            if itemP < itmCnt:
                print(",", end="")
        print("]")
        return
        
    def printRules(self):
        print("SM Rules:")
        rn = 1
        for key, value in self.SMRules.items():
            print("Rule",rn,"%4s" % key,"|", value) 
            rn += 1         
        return
       
        
def printRules(self):
        print("SM Rules:")
        rn = 1
        for key, value in self.SMRules.items():
            print("Rule",rn,"%4s" % key,"|", value) 
            rn += 1         
        return
    def printStep():
        """ print out each  step of the process"""
        def getInputString():
            """ get input to determine if it is a palindrome"""
            def processString(string,Stk):
                """Process the input string to determine if it is a plindrome"""
                def main():
                    """You might have something like the following"""
                    pString = getInputString()
                    Stk = StackMachine()
                    processString(pString,Stk) 
    
if __name__ == '__main__':
    main()
    
