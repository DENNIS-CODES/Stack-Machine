## Stack-Machine

- A stack machine is a kind of `automaton` that uses a stack for auxiliary data storage. The size of the stack  is  `unbounded`—it  never  runs  out  of  `space` and  that  gives `stack machines`  an  edge  over  `fi nite  automata`.  In  effect,  stack  machines  have `infinite memory`, though they must use it in `stack order` following the `LIFO principle`.
- `Data` is available at the `Top` of the stack by `standard` inside the stack machine. `Push` and `pop` instructions are used to get `data` and `instructions` from the stack, which functions both as a `resource` and a `terminal`. The `input` and `output` addresses are not required because the `default address` is at the `Top` of the stack. So no need to pass `specific addresses`   in the stack machine instruction.
- As a result, the `OPCODE (Operation Code)` field is the only field in the `instruction format`. This   `instruction format` is known as `Zero address` instruction.
- There are two basic operations performed in a Stack:

1. `Push()`
2. `Pop()`

. `Push()` function is used to `add` or `insert` new elements into the stack.

. `Pop()` function is used to `delete` or `remove` an element from the stack.
- When a stack is `completely full`, it is said to be `Overflow state` and if stack is `completely empty`, it is said to be `Underflow state`.
- Stack allows operations at `one end only`. Stack behaves like a real life `stack\pile`, for example, in a `real life`, we can `remove` one `plate` or `dish` from the `Top` of   the stack only or while playing a `deck of cards`, we can `place` or `remove` a card from top of the stack only.
- Similarly, here also, we can only access the `Top` element of a stack.
  According to its `LIFO structure`, the element which is `inserted last`, is `accessed first`.

![image](https://user-images.githubusercontent.com/65861136/121089250-8ce71e00-c7ef-11eb-8932-32275c5757fd.png)


Position of Top|Status of Stack
|--------|--------|
|-1|Stack is empty.|
|0|	Only one element in a stack.|
|N| - 1	Stack is full.|
|N|	Stack is overflow. (Overflow state)|

In The Above files `StackMachine.py` contains class `StackMachine()` which Describes the Function of the stack machine

- The __init__() dunder method is the constructor and initializes an empty list (we use list instead of the array in Python).
- Push method append a new data element on the top of the Stack.
- Pop method removes the last element and returns it.
- We need to check underflow condition in the Pop method, this is why we implement isEmpty method. The method isEmpty verify that the array is not empty before performing the     Pop operation.
Note: We didn’t implement the check overflow method because Python lists have dynamic length (it keeps growing). In other programming language you need to implement it.

Here is a quick logic to check overflow condition.
```
check_overflow()
    return size(array_used_in_stack)== maximum
```
If Stack is full and we try to push a new data element it gives Stackoverflow error.

Stack can be defined using array in C++ as follows:
```
typedef struct stack
     {
          int element [MAX];   
          int top;
     }stack;
```  
I was Supposed to implement the class Stack Machine() to check wether user `input` is a `palindrome` or not 
## Approach:  

- Find the length of the string say len. Now, find the mid as mid = len / 2.
- Push all the elements till mid into the stack i.e. str[0…mid-1].
- If the length of the string is odd then neglect the middle character.
- Till the end of the string, keep popping elements from the stack and compare them with the current character i.e. string[i].
- If there is a mismatch then the string is not a palindrome. If all the elements match then the string is a palindrome.

File `PalindromeChecker.py` contains the `implementation` of the above `approach`

## Exetension
I aslo tried out a program that checks if user input has balanced parenthesis
