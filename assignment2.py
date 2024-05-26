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
    

    