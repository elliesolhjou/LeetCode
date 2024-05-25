'''
Write a function to reverse a string or array using a stack.

'''

myString = "abcd"
def revString(str):
    # using stack
    # array
    # LIFO
    stack=[]
    for char in str:
        stack.append(char)
    # stack = stack[::-1]
    print (stack)
    revData = []
    n = len(stack)
    for i in range(n):
        revData.append(stack[(n-1)-i])
    print (revData)
    result = ''.join(revData)
    return result

print(revString("abcd"))
