'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''
from collections import deque
# from collections import queue



class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def arrayToTree(arr):
    if not arr:
        return None
    roots = TreeNode(arr[0])
    # print(roots)
    # print([roots])
    queue = deque([roots])
    print(queue)
    print(arr)

    i = 1
    while i<len(arr):
        # grab first treenode
        current = queue.popleft()
        # current is first pointer to traverse our tree
        # i is second pointer to traverse our input array
        if arr[i]:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i+=1
        
        if arr[i]:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i+=1

    return roots

def leafPath(root, path=[], paths=[]):

    # define base case
    if not root:
        return 
    # there is value to node
    path.append(root.val)
    print(f" this is path {path}")

    # check if we reached to leaf (DFS) then add it to one of the path of paths
    if not root.left and not root.right:
        # creating list of arrays within an array
        paths.append(list(path))
        print(paths)
    else:
        # direct pointer and recursive call to left sub trees
        leafPath(root.left, path)
        leafPath(root.right, path)

    
    # Backtrack by removing the current node's value
    # path.pop()






# a = [5,4,8,11,None, 13,4,7,2,1]
a = [5,4,8,11,None,13,4,7,2,None,None,None,1]
root = arrayToTree(a)
paths=[]
leafPath(root)
print(paths)
