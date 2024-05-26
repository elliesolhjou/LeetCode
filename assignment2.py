"""
(15 points) 
Write a description and at least two examples (in real life and in programming) for:
Stacks
Queues
Deques
"""
# Stacks:
# A stack is a linear data structure that follows the Last In, First Out (LIFO) principle, 
# meaning the last element added to the stack will be the first one to be removed. This structure 
# is analogous to a stack of plates in a cafeteria, where you put plates on top of the stack and take
# the top plate off when serving. 
# In programming, a common use of a stack is the "undo" feature in 
# text editors, which reverses the most recent actions first, based on the LIFO principle.

# Queues:
# A queue is a linear data structure that follows the First In, First Out (FIFO) principle, 
# where the first element added is the first one to be removed. This can be seen in real life as 
# a line of people waiting to buy tickets at a movie theater, where the first person in line is served 
# first. In programming, a queue is used for tasks like printing documents, where documents are printed 
# in the order they were sent to the printer.

# Deques (Double-Ended Queues):
# A deque is a type of queue that allows insertion and removal of elements
#  from both the front and the back, making it a highly flexible data structure. 
# In real life, this is similar to a deck of cards where you can add or remove a 
# card from either the top or bottom of the deck. A programming example of a deque 
# is a playlist application, where you can add songs to either the beginning or end 
# of the playlist and also remove them from either end, providing a flexible way to manage the playlist.
# -------------------------------------------------------------------------------------------------------------#
from dsa import pretty_print
'''
2. (25 points) Write a function that returns a Boolean as to whether a 
string has balanced braces. You may ignore non-bracket characters. 
For our purposes, the following are bracket characters:

(){}[]
For example, this function should return True for the following: 

[ ]

{}{}[]()

[{()}]

(()[[[()({})]]])

It should return False for the following:

[ ] [

{{}[](})

[{)}]

(()[()({})]]])
'''
# In balanced brackets, the closing brackets should matched teh immediate opening one
def balancedBrackets(str):
    brackets = {
        "}":"{",
        "]":"[",
        ")":"("
    }
    # we define stack bc brackets order comes in LIFO
    stack=[]
    if len(str) % 2 != 0:
        return False
    # first iterate
    for char in str:
        # if it is opening bracket (best case)
        if char in brackets.values():
            stack.append(char)
        # if it is closing bracket
        elif char in brackets:
            # check char's corresponding opening bracket is in stack or not
            # peek or top for stack
            # the closing brackets should match the soonest opening
            if not stack or stack[-1] != brackets[char]:
                print ("False, not matching brackets")
                return False

            # found corresponding open bracket
            stack.pop()
    if not stack:
        # there are not matching pair
        return  True
    else:
        return False
    


print(balancedBrackets("[{()}]"))
# print(balancedBrackets("[{()}]"))
# print(balancedBrackets("[{()}]"))
print(balancedBrackets("(()[()({})]]])"))

# for practice
def balancedBrackets(str):
    # in balanced brackets, the closing bracket should match
    # the nearest opening brackets
    brackets={
        "]":"[",
        "}":"{",
        ")":"(",
    }
    # brackets come in LIFO -> stacks
    stack=[]
    for char in str:
        # best case: if it i opening bracket
        if char in brackets.values():
            stack.append(char)
        # if it is closing brackets
        elif char in brackets:
        # if it is closing and not matching to teh latest opening
        # latest opening is stack top
            if not stack or stack[-1] != brackets[char]:
                return False
        # if closing matches top stack 
        stack.pop()

    if not stack:
        return True
    else:
        return False
    
# -------------------------------------------------------------------------------------------------------------#
'''
3. (35 points) Fully implement the Deque data structure (you may choose either a static or dynamic implementation) using an array.  Do not use any built-in methods except for the index operator. Also, do not simply write a wrapper to the built-in Deque class.
It should have the following methods:
append_left(element)
append_right(element)
pop_left()
pop_right()
peek_left()
peek_right()
get_count()
It may also be helpful to implement a print method to display the contents of the deque in the correct order.
Make sure to test your code, especially for tricky situations.
'''
from dsa import pretty_print
from dsa import queue

class Deque:
    def __init__(self):
        # define array
        self.items=[]
        # create size (count of index)
        self.size = 0
    def append_left(self, element):
        # create new array with new size (adding one element every time appending = increasing size) in cpu
        new_items = [None] * (self.size+1)
        # assign first left cell to the element
        new_items[0] = element
        # Copy the existing elements to the new array, starting from index 1
        # shifting rest of previous elements to right
        for i in range(1, self.size+1):
            new_items[i] = self.items[i-1]
        self.items = new_items
        self.size +=1
    def append_right(self, element):
        # growing array -> creating new array with new size
        new_items = [None] * (self.size+1)
        # assign last cell of array on right to element
        new_items[self.size] = element
        # Copy the existing elements to the new array, starting from index 0
        for i in range(self.size+1):
            new_items[i] = self.items[i]
        self.items= new_items
        self.size+=1
    
    # pop return element
    def pop_left(self): 
        # if queue is empty raise an error
        if not self.size == 0:
            raise IndexError("empty queue")
        # grab value of popped element
        element = self.items[0]
        # create new array with new size
        new_items= [None] * (self.size-1)
        # shift elements to right
        for i in range(1, self.size-1):
            new_items[i-1] = self.items[i]
        self.items = new_items
        self.size -=1
        return element

    def pop_right(self):
        # return value
        # if queue is empty
        if self.size == 0:
            raise IndexError("empty stack")
        # grab return value
        element = self.items[self.size-1]
        # create new array
        new_items = [None]* (self.size-1)
        # copy old array elements to new array
        for i in range(self.size-1):
            new_items[i] = self.items[i]
        
        new_items = self.items
        self.size -=1
        return element

    def peek_left(self):
        # return value
        # check size
        if self.size == 0:
            raise IndexError ("empty queue")
        element = self.items[0]
        return element
    
    def peek_right(self):
        if self.size == 0:
            raise IndexError ("empty queue")
        return self.items[self.size-1]

    def get_count(self):
        return self.size
    
    def __str__(self):
        return str(self.items[:self.size])
    

# -------------------------------------------------------------------------------------------------------------#
'''4. (25 points) Write a recursive binary search function to search for an element in an array. Assume the elements in the array are sorted.
It should return the index of the element and return -1 if it is not found.'''

# define base case
# define recursive call
# binary search is L, R mid

def recursiveBinarySearch(arr, target, low, high):
    # define base case
    if low>high:
        return -1
    mid = (low+high)//2
    if arr[mid] == target:
        return mid
    # start binary search
    elif target > arr[mid]:
        return recursiveBinarySearch(arr, target, mid+1, high)
    else:
        return recursiveBinarySearch(arr, target, low, mid-1)

def search(arr, target):
    # helper function bc we don't ask for low and high from people
    return (recursiveBinarySearch(arr, target, 0, len(arr)-1))

print(search([1,2,4,5,6],17))
                                                     












# -------------------------------------------------------------------------------------------------------------#