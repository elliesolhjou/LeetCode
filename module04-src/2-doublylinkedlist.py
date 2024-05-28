#!/usr/bin/env python
# coding: utf-8

# Create a doubly linked list

# In[ ]:


from dsa.doublylinkedlist import DoublyLinkedList, Node


# In[ ]:


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)


# In[ ]:


n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3


# In[ ]:


dlink = DoublyLinkedList(n1, n4, 4)


# Traversal

# In[ ]:


def print_list(link):
    if link is None:
        print()
    else:
        print(link.value, end=" ")
        print_list(link.next)
        
print_list(dlink.head)


# In[ ]:


def print_reverse_list(link):
    if link is None:
        print()
    else:
        print(link.value, end=" ")
        print_reverse_list(link.prev)
        
print_reverse_list(dlink.tail)


# insert operations

# prepend

# In[ ]:


print_list(dlink.head)


# In[ ]:


new_node = Node(5)
new_node.next = dlink.head
dlink.head.prev = new_node
dlink.head = new_node
dlink.count += 1


# In[ ]:


print_list(dlink.head)


# In[ ]:


print_reverse_list(dlink.tail)


# ##### append

# In[ ]:


print_list(dlink.head)


# In[ ]:


new_node = Node(50)
new_node.prev = dlink.tail
dlink.tail.next = new_node
dlink.tail = new_node
dlink.count += 1


# In[ ]:


print_list(dlink.head)
print_reverse_list(dlink.tail)


# ##### insert middle

# In[ ]:


print_list(dlink.head)


# In[ ]:


dlink.head.next.next.next.value


# In[ ]:


new_node = Node(25)
current = dlink.head.next.next.next
new_node.next = current
new_node.prev = current.prev
current.prev = new_node
new_node.prev.next = new_node
dlink.count += 1


# In[ ]:


print_list(dlink.head)
print_reverse_list(dlink.tail)


# #### delete

# ##### delete head

# In[ ]:


print_list(dlink.head)


# In[ ]:


dlink.head = dlink.head.next
dlink.head.prev.next = None
dlink.head.prev = None
dlink.count -= 1


# In[ ]:


print_list(dlink.head)
print_reverse_list(dlink.tail)


# ##### delete tail

# In[ ]:


print_list(dlink.head)


# ###### search for second to the last node

# In[ ]:


dlink.tail.prev.value


# In[ ]:


current = dlink.tail.prev


# In[ ]:


current.next = None
dlink.tail = current


# In[ ]:


dlink.count -= 1


# In[ ]:


print_list(dlink.head)
print_reverse_list(dlink.tail)


# ##### delete middle

# In[ ]:


print_list(dlink.head)


# look for node be deleted (delete 25)

# In[ ]:


dlink.head.next.next.value


# In[ ]:


current = dlink.head.next.next


# In[ ]:


current.value


# In[ ]:


current.prev.next.value


# In[ ]:


current.prev.value


# In[ ]:


current.prev.next = current.next
current.next.prev = current.prev
current.next = None
current.prev = None
dlink.count -= 1


# In[ ]:


print_list(dlink.head)
print_reverse_list(dlink.tail)
dlink.count


# DSALinkedList Operations

# In[ ]:


from dsa.doublylinkedlist import DoublyLinkedList, Node


# In[ ]:


dlink = DoublyLinkedList.from_array([10, 20, 30, 40])


# In[ ]:


dlink


# insert front (prepend)

# In[ ]:


dlink.insert(0, 5)


# In[ ]:


dlink


# ##### insert middle

# In[ ]:


dlink.insert(3, 25)


# In[ ]:


dlink


# ##### insert tail (append)

# In[ ]:


dlink.tail.value


# In[ ]:


dlink.append(50)


# In[ ]:


dlink


# In[ ]:


dlink.tail.value


# In[ ]:


print_reverse_list(dlink.tail)


# Delete Operations

# delete head

# In[ ]:


dlink.delete(0)


# In[ ]:


dlink


# delete middle

# In[ ]:


dlink.delete(2)


# In[ ]:


dlink


# delete tail

# In[ ]:


dlink.delete(4)


# In[ ]:


dlink


# In[ ]:


print_reverse_list(dlink.tail)


# In[ ]:




