class MyStack:

    def __init__(self):
        self.myStack=[]


    def push(self, x: int) -> None:
        return self.myStack.append(x)
        
    def pop(self) -> int:
        return self.myStack.pop()
        
    def top(self) -> int:
        return self.myStack[-1]
        

    def empty(self) -> bool:
        if len(self.myStack) == 0:
            return True
        else: return False

myStack = MyStack( )
print(myStack.push(1))
print(myStack.push(2))
print(myStack.pop())