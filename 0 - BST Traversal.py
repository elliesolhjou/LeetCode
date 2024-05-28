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
    BFS <--> QUEUE
    WHILE LOOP
'''
from collections import deque
help(deque)
def bfs(root):
    queue = deque()
    if root:
        queue.append(root)
    level = 0
    visit=set()
    while queue:
        print(level)
        for i in range(len(queue)):
            current_pointer = queue.popleft()
            # after popping node -> add its value to a place holder array/set would help a lot
            visit.add(current_pointer.value)
            if current_pointer.left:
                # add to queue to go over on those in next iterations
                queue.append(current_pointer.left)
            if current_pointer.right:
                queue.append(current_pointer.right)
            
        level+=1
    return level
