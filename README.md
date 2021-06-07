## Stack-Machine

A stack machine is a kind of automaton that uses a stack for auxiliary data storage. The size of the stack  is  unbounded—it  never  runs  out  of  space—and  that  gives  stack machines  an  edge  over  fi nite  automata.  In  effect,  stack  machines  have infinite memory, though they must use it in stack order.
Data is available at the top of the stack by convention inside the stack machine. Push and pop instructions are used to get data and instructions from the stack, which functions both as a resource and a terminal. The input and output addresses are not required because the default address is at the top of the stack. So no need to pass specific addresses in the stack machine instruction.
There is no need to pass explicit addresses in the stack machine instruction. As a result, the OPCODE (Operation Code) field is the only field in the instruction format. This instruction format is known as Zero address instruction.
- The two operations of the stack are insertion (push) and deletion (pop) of items in the Stack.However, nothing physical is pushed or popped in a computer stack.
  Perform the following set of instructions intended for execution on a stack machine:
> PUSH B, 
> PUSH X, 
> ADD, 
> POP C, 
> PUSH C, 
> PUSH Y, 
> SUB, 
> POP Z 

First PUSH B and X in a stack, 
- then to add first POP X 
- then B, ADD (B+X), 
- POP C=B+X (no data with name C, so the data present is stored in variable C)
- then POP C.
Similarly, to perform SUB (Y-C) first perform POP operation POP as Z. See in figure below for better understanding:


Alphabet|table
|--------|--------|
|--------|---------|
A stack machine M is a 4-tuple M = (*, 6, S, G), where* is the stack alphabet6 is the input alphabetS* is the initial stack symbolG ((6 {ε}) u*oP(**)) is the transition function

![image](blob:file:///1cb4cee0-2965-4c42-ab28-442a893336fc)
