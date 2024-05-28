# ========================================================================================================#
#                                      BST - DFS - O(LOG N)
# ========================================================================================================#

'''
    - DFS -> inorder (left(small)<root<right(large))
    - DFS -> preorder (root<left(small)<right(large))
    - DFS -> reverse (right<roo<left)

    DFS <--> RECURSION OR STACK
'''
from dsa.tree  import Node

# help(tree)
root = Node(0)

def dfs_inorder(root):
    if not root: 
        return 
    dfs_inorder(root.left)
    print(root.value)
    dfs_inorder(root.right)

def dfs_reverse(root):
    if not root:
        return
    dfs_reverse(root.right)
    print(root.value)
    dfs_reverse(root.left)

def dfs_preorder(root):
    if not root:
        return
    print(root.value)
    dfs_preorder(root.left)
    dfs_preorder(root.right)


# ========================================================================================================#
#                                      BST - BFS - O(N)
# ========================================================================================================#
'''
    DFS <--> QUEUE


'''
from collections import deque

