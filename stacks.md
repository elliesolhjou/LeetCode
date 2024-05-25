What are Stacks?

• Efficient, commonly used **data structures**
• Have elements that are LIFO – Last in, First Out
• **Can be implemented using arrays or linked lists**
• Limit number operations, limit number of bugs

Stack Applications:
• Function Calls
• Undo/Redo Feature
• Browser Navigation
• Storage of Temporary data

**Static Stack Representation has two features, capacity and top**
• **array**
container for stack

• **capacity**
maximum number of elements in the stack

• **top of the stack**
-1 to represent the top of an empty stack

**Stack Operations**
Operation Description
**Push** add element at the top
**Pop** get and remove element at the top
**Peek** get the element at the top(-1)
**Count** get the number of elements

Set top to -1 since the stack is empty
initiate a stack with giving a capacity and top = -1

![alt text](image.png)
when top is -1 means there is stack but it is empty
when peek value (top) returns as a non -1 value -> it would be
the value stored at top of stack
![alt text](image-1.png)
top is changing to the latest value pushed to the stack
![alt text](image-2.png)

**BIG O**
![alt text](image-3.png)
