#!/usr/bin/env python
# coding: utf-8

# Create a Linked List

# In[ ]:


from dsa.singlylinkedlist import LinkedList, Node


# In[ ]:


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n1.next = n2
n2.next = n3
n3.next = n4


# In[ ]:


link = LinkedList(n1, n4, 4)


# In[ ]:


link.head.value


# In[ ]:


link.tail.value


# In[ ]:


link.head.next.value


# In[ ]:


link.head.next.next.next.value


# In[ ]:


link.tail.next


# #### traverse a linked list

# In[ ]:


def print_list(node):
    if node is None:
        print()
    else:
        print(node.value, end=" ")
        print_list(node.next)
        
print_list(link.head)


# In[ ]:


def print_iter(linkedlist):
    current = linkedlist.head
    while current != None:
        print(current.value, end=" ")
        current = current.next
    print()
    
print_iter(link)
    


# #### insert 
# * note: counts not updated for simplicty

# ##### prepend

# In[ ]:


print_iter(link)


# In[ ]:


new_node = Node(5)
new_node.next = link.head
link.head = new_node


# In[ ]:


print_iter(link)


# ##### append

# In[ ]:


print_iter(link)


# In[ ]:


new_node = Node(50)
link.tail.next = new_node
link.tail = new_node


# In[ ]:


print_iter(link)


# ##### insert middle

# In[ ]:


print_iter(link)


# In[ ]:


link.head.next.next.value


# In[ ]:


new_node = Node(25)
current = link.head.next.next
new_node.next = current.next
current.next = new_node


# In[ ]:


print_iter(link)


# #### delete
# * note: counts not updated for simplicity

# ##### delete head

# In[ ]:


print_iter(link)


# In[ ]:


current = link.head
link.head = link.head.next
current.next = None


# In[ ]:


print_iter(link)


# ##### delete tail

# In[ ]:


print_iter(link)


# ###### search for second to the last node

# In[ ]:


link.head.next.next.next.next.value


# In[ ]:


current = link.head.next.next.next.next


# In[ ]:


current.next = None
link.tail = current


# In[ ]:


print_iter(link)


# ##### delete middle

# In[ ]:


print_iter(link)


# look for node before to be deleted

# In[ ]:


link.head.next.value


# In[ ]:


current = link.head.next
next = current.next


# In[ ]:


current.next = current.next.next
next.next = None


# In[ ]:


print_iter(link)


# DSALinkedList Operations

# In[ ]:


from dsa.singlylinkedlist import LinkedList, Node


# In[ ]:


link = LinkedList.from_array([10, 20, 30, 40])


# In[ ]:


link


# ##### insert front (prepend)

# In[ ]:


link.insert(0, 5)


# In[ ]:


link


# ##### insert middle

# In[ ]:


link.insert(2, 25)


# In[ ]:


link


# ##### insert tail (append)

# In[ ]:


link.tail.value


# In[ ]:


link.append(50)


# In[ ]:


link


# In[ ]:


link.tail.value


# ##### delete head

# In[ ]:


link.delete(0)


# In[ ]:


link


# ##### delete middle

# In[ ]:


link.delete(1)


# In[ ]:


link


# ##### delete tail

# In[ ]:


link.delete(4)


# In[ ]:


link


# In[ ]:




