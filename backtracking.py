'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def arrayToTree(arr):
    if not root:
        return False
    TreeNode
def leafPath(root, path=[]):
    TreeNode(root)
    # define base case
    if not root:
        return False
    # there is value to node
    path.append(root.val)

    # check if we reached to leaf (DFS)
    if not root.left and not root.right:
        return True
    # direct pointer and recursive call to left sub trees
    if leafPath(root.left, path):
        return True
    if leafPath(root.right, path):
        return True
    
    path.pop()
    return False





root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
leafPath(root)