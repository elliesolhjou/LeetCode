'''
Write a function that accepts an array and converts it to a linked list.'''

class Node:
    def __init__(self, value, next= None ):
        self.value = value
        self.next = next



def linkListMaker(arr):
    if not arr:
        return None
    head = Node(arr[0])
    # pointer
    current = head
    for val in arr:
        # create node
        current.next = Node(val)
        # move pointer
        current = current.next
    
    return head


print(linkListMaker([1,5,3,5,7,8]))

