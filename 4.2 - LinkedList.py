'''
Write a function to detect a cycle in a linked list.
'''
class Node:
    def __init__(self, val, next= None):
        self.value = val
        self.next = next

listNode1 = Node(4)
listNode2 = Node(5)
listNode3 = Node(6)
listNode4 = Node(7)

listNode1.next = listNode2
listNode2.next = listNode3
listNode3.next = listNode4
listNode4.next = listNode1

def detectCycle (node):
    current = node
    visited = set()
    while current != None:
        print(current.value)
        current = current.next
        if current not in visited:
            visited.add(current)
        else:
            return "Cycle Detected"


print(detectCycle(listNode1))