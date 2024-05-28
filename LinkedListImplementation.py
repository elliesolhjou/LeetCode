# LinkedList are made of listNodes (nodes)

# BUILDING LIST NODE IMPLEMENTATION
class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next= next

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
# -----------------------------------------------------------------------------
#  APPENDING NODE IN DOUBLE LINKED LIST O(1)
# assign new node to tails next property
tail.next = double_node4
# assign new nodes' prev to tail
double_node4.previous = tail
# move/update tail pointer
tail = tail.next
#  or 
tail = double_node4
# -----------------------------------------------------------------------------
# REMOVING NODES ON ENDS O(1)
# assign new node
double_node3 = tail.previous
# make it tail
double_node3.next = None
# move pointer
tail = double_node3

# -----------------------------------------------------------------------------
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



# -----------------------------------------------------------------------------
# To create a function that takes two linked 
# lists and outputs their union efficiently, we can use a set to keep track of the unique elements. This way, we can ensure that each element only appears once in the resulting linked list. Here's the code to achieve this:
def linkListMaker(arr):
    if not arr:
        return None
    head = Node(arr[0])
    # pointer
    current = head
    for val in arr[1:]:
        # create node
        current.next = Node(val)
        # move pointer
        current = current.next
    
    return head


def unionMaker(arr1, arr2):
    head1 = linkListMaker(arr1)
    head2 = linkListMaker(arr2)
    if not head1 and not head2:
        return None
    
    unique_nodes = set()
    current = head1
    while current:
        unique_nodes.add(current.value)
        current = current.next
    
    current = head2
    while current:
        unique_nodes.add(current.value)
        current = current.next

    unique_nodes = list(unique_nodes)

    return linkListMaker(unique_nodes)

# -----------------------------------------------------------------------------
# Function to print the linked list for testing purposes
def printLinkedList(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# -----------------------------------------------------------------------------
# reverse linked list
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

# -----------------------------------------------------------------------------
#  double linked list
class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")
# -----------------------------------------------------------------------------
#  reverse double linked list
    def reverse(self):
        current = self.head
        while current:
            # Swap the next and prev pointers
            current.prev, current.next = current.next, current.prev
            # Move to the next node (which is actually the previous node due to the swap)
            current = current.prev

        # Swap the head and tail
        self.head, self.tail = self.tail, self.head

# Test the reverse function
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)

print("Original list:")
dll.print_list()

dll.reverse()

print("Reversed list:")
dll.print_list()
