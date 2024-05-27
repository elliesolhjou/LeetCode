'''
Given a Tree and Node classes without any methods except for constructors, build a binary search tree.
No need to write the insert method. Instead, 
build the tree node by node (construct a nodes and link them appropriately).
You are given the following sequence:
42, 23, 55, 17, 45, 30, 8
'''

class Node:
    def __init__ (self,value, left=None, right= None):
        self.root = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root):
        self.root = root

root = Node(42)
root.left = Node(23)
root.left.right = Node(30)
root.left.left = Node(17)
root.left.left.left = Node(8)
root.right = Node(55)
root.right.left= Node(45)


tree = Tree(root)





