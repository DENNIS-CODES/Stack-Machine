## Stack-Machine

- A stack machine is a kind of automaton that uses a stack for auxiliary data storage. The size of the stack  is  unbounded—it  never  runs  out  of  space—and  that  gives  stack machines  an  edge  over  fi nite  automata.  In  effect,  stack  machines  have infinite memory, though they must use it in stack order.
- Data is available at the top of the stack by convention inside the stack machine. Push and pop instructions are used to get data and instructions from the stack, which functions   both as a resource and a terminal. The input and output addresses are not required because the default address is at the top of the stack. So no need to pass specific addresses   in the stack machine instruction.
- There is no need to pass explicit addresses in the stack machine instruction. As a result, the OPCODE (Operation Code) field is the only field in the instruction format. This     instruction format is known as Zero address instruction.
- There are two basic operations performed in a Stack:

1. Push()
2. Pop()

. Push() function is used to add or insert new elements into the stack.

. Pop() function is used to delete or remove an element from the stack.
- When a stack is completely full, it is said to be Overflow state and if stack is completely empty, it is said to be Underflow state.
- Stack allows operations at one end only. Stack behaves like a real life stack, for example, in a real life, we can remove a plate or dish from the top of the stack only or     while playing a deck of cards, we can place or remove a card from top of the stack only.
- Similarly, here also, we can only access the top element of a stack.
  According to its LIFO structure, the element which is inserted last, is accessed first.

![image](https://user-images.githubusercontent.com/65861136/121089250-8ce71e00-c7ef-11eb-8932-32275c5757fd.png)


Position of Top|Status of Stack
|--------|--------|
|-1|Stack is empty.|
|0|	Only one element in a stack.|
|N| - 1	Stack is full.|
|N|	Stack is overflow. (Overflow state)|

- Stack can be implemented using one-dimensional array. One-dimensional array is used to hold elements of a stack. Implementing a stack using array can store fixed number of data values. In a stack, initially top is set to -1. Top is used to keep track of the index of the top most element.

Stack can be defined using array as follows:
```
typedef struct stack
     {
          int element [MAX];   
          int top;
     }stack;
```     
