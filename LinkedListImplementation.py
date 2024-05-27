# LinkedList are made of listNodes (nodes)

# BUILDING LIST NODE IMPLEMENTATION
class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next= None

listNode1 = Node(4)
listNode2 = Node(5)
listNode3 = Node(6)
listNode4 = Node(7)

# LINKING NODES
listNode1.next = listNode2
listNode2.next = listNode3
print(listNode1.next)

# ITERATING THROUGH LINKEDLIST O(N)
current = listNode1
while current != None:
    print(current.value)
    current = current.next

#  HEAD == TAIL -> LINKEDLIST OF SIZE 1

# APPENDING TO LINKED LIST O(1)
    # ASSIGN NEW NODE TO TAIL NEXT PROPERTY
    tail = listNode3
    tail.next = listNode4
    # MOVE TAIL POINTER
    tail = tail.next
    # or 
    tail = listNode4


head = listNode1
# REMOVING NODELIST FROM ENDS OF LINKEDLIST O(1)
head.next = head.next.next
# REMOVING NODELIST FROM ANYWHERE OF LINKEDLIST O(N)



# DOUBLY LINKED LIST
class DoubleLinkedNode:
    def __init__(self, val, prev=None, next= None):
        self.value = val
        self.previous = prev
        self.next = next

double_node1 = DoubleLinkedNode(1)
double_node2 = DoubleLinkedNode(2)
double_node3 = DoubleLinkedNode(3)
double_node4 = DoubleLinkedNode(4)

print(double_node1.next)
head = double_node1
head.next = double_node2
double_node2.next = double_node3
double_node2.previous = head
double_node3.previous = double_node2
tail = double_node3

# print(head.next.value)
# print(tail.prev)

#  APPENDING NODE IN DOUBLE LINKED LIST O(1)
# assign new node to tails next property
tail.next = double_node4
# assign new nodes' prev to tail
double_node4.previous = tail
# move/update tail pointer
tail = tail.next
#  or 
tail = double_node4

# REMOVING NODES ON ENDS O(1)
# assign new node
double_node3 = tail.previous
# make it tail
double_node3.next = None
# move pointer
tail = double_node3



def reverse_linkedlist(llist):
    current = llist.head
    prev = None
    llist.tail = llist.head
    while current != None:
        next = current.next
        current.next = prev

        prev = current
        current = next
    llist.head = prev
        
reverse_linkedlist(llist)
print_iter(llist)