#!/usr/bin/env python
# coding: utf-8

# Create a Tree

# In[ ]:


from dsa.tree import Node, Tree
from dsa.pretty_print import tree_print


# In[ ]:


n1 = Node(50)
tree = Tree(n1)
tree_print(tree)


# insert

# In[ ]:


tree.insert(45)


# In[ ]:


tree_print(tree)


# In[ ]:


tree.insert(30)


# In[ ]:


tree.insert(75)


# In[ ]:


tree_print(tree)


# In[ ]:


tree.insert(77)


# In[ ]:


tree.insert(55)


# In[ ]:


tree_print(tree)


# Search

# In[ ]:


tree.search(30)


# In[ ]:


tree.search(33)


# In[ ]:


tree_print(tree)


# delete

# In[ ]:


tree.delete(30)
tree_print(tree)


# In[ ]:


tree.delete(50)
tree_print(tree)


# In[ ]:


tree.delete(77)
tree_print(tree)


# inefficient tree

# In[ ]:


tree = Tree()
for e in [10, 20, 30, 40, 50]:
    tree.insert(e)


# In[ ]:


tree_print(tree)


# In[ ]:





# In[ ]:


tree = Tree()
for e in [60, 50, 40, 30, 20, 10]:
    tree.insert(e)


# In[ ]:


tree_print(tree)


# In[ ]:




