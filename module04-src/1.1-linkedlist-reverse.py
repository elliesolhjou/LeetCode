#!/usr/bin/env python
# coding: utf-8

# Create a Linked List

# In[2]:


from dsa.singlylinkedlist import LinkedList, Node


# In[ ]:


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n1.next = n2
n2.next = n3
n3.next = n4

llist = LinkedList(n1, n4, 4)


# In[ ]:


def print_iter(llist):
    current = llist.head
    while current:
        print(current.value, end=" ")
        current = current.next
    print()
    
print_iter(link)
    


# Reverse a Linked List (iterative version)

# In[ ]:


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


# In[ ]:


reverse_linkedlist(llist)
print_iter(llist)


# reverse linked list (recursive version)

# In[4]:


def reverse_linkedlist_recursive(llist):
    llist.tail = llist.head
    llist.head = reverse_node_recursive(llist.head)
    
def reverse_node_recursive(node):
    if node is None or node.next is None:
        return node
    
    rest = reverse_node_recursive(node.next)

    # set the next node's next reference to the current node
    # A->B to B<-A
    node.next.next = node
    node.next = None
 
    return rest

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n1.next = n2
n2.next = n3
n3.next = n4
llist = LinkedList(n1, n4, 4)
print(llist, llist.head.value, llist.tail.value)
reverse_linkedlist_recursive(llist)
print(llist, llist.head.value, llist.tail.value)


# In[24]:


def display_node(node):
    if not node:
        print("X")
    else:
        next_value = "X" if node.next is None else node.next.value
        print(f"{node.value}->{next_value}")

def reverse_linkedlist_recursive(llist):
    llist.tail = llist.head
    llist.head = reverse_node_recursive(llist.head)
    
def reverse_node_recursive(node):
    if node is None or node.next is None:
        print("returning node")
        return node

    print("recursing ", node.value)
    rest = reverse_node_recursive(node.next)
    display_node(node.next.next)
    display_node(node.next)
    display_node(node)
    display_node(rest)
    node.next.next = node
    print("flip")
    display_node(node.next.next)
    display_node(node.next)
    display_node(node)
    node.next = None
 
    return rest

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n1.next = n2
n2.next = n3
llist = LinkedList(n1, n3, 3)
print(llist, llist.head.value, llist.tail.value)
reverse_linkedlist_recursive(llist)
print(llist, llist.head.value, llist.tail.value)


# In[ ]:




