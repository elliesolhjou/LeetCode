'''
Write a function that accepts a binary tree and return a new copy of it. The copy should have exactly the same values and structure.
'''


from dsa.tree import Node 
#from dsa.tree import Tree 
# help(Node)class Node(builtins.object) 
def btCopy(root): 
    if not root: 
        return None 
    copy_root = Node(root.value) 
    copy_root.left = btCopy(root.left) 
    copy_root.right = btCopy(root.right) 
    
    return copy_root 

root= Node(3) 
node1= Node(1) 
node2= Node(2) 
node3= Node(3) 
root.left = node1 
node1.left = node3 
root.right = node2 
print(btCopy(root))