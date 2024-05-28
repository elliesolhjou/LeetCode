class Tree:
    def __init__(self, root):
        self.root = root
# ========================================================================================================#
#                                         CREATE NODE
# ========================================================================================================#
class TreeNode:
    def __init__(self, value, left= None, right= None):
        self.value = value
        self.left = left
        self.right = right
# ========================================================================================================#
#                                       INSERT NODE - O(N)
# ========================================================================================================#

    # INSERTION
    def insert(self, root, value):
        # base case 
        if not root:
            return TreeNode(value)
        if value > root.value:
            root.right = self.insert(root.right, value)
        elif value < root.value:
            root.left = self.insert (root.left, value)
        
        return root

# ========================================================================================================#
#                                        DELETE A NODE - O(LOG N)
# ========================================================================================================#
    # DELETION A NODE -
    def delete(self, root, value):
        if not root:
            return None
        if value > root.value:
            root.right = self.delete(root.right, value)
        elif value< root.value:
            root.left = self.delete(root.left, value)
        #  the deletion will return the value/ node of new node replacing 
        #  the deleted node
        else:
            # simple case
            #  if it has 1 child it would fill the deleted root value place - lifted up
            #  we check if it has either left or right child
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            
            # hard case - deleted 2 child node 
            else:
                # it has two child so we have to fin minvalue of them and replace it
                #  it is safe to replace with : 
                # 1. min nodes on right side of entire tree (better bu not matter)
                # or 2. largest value from left side of whole tree (BST satisfied in entire tree)
                minNode = self.minValueNode(root.right)
                #  we fill out the deleted node value now with minNode found right side
                root.val = minNode.val
                # then recursive delete call for subtrees under minNode 
                # since it is moved and it is unordered
                root.right = self.delete(root.right, minNode.val)
            return root

# ========================================================================================================#
#                                       FIND MIN VALUE - O(LOG N)
# ========================================================================================================#
        
    # FIND MIN VAL
    def minValueNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
# ========================================================================================================#
#                                     FIND MAX VALUE - O(LOG N)
# ========================================================================================================#
    # FIND MAX VAL
    def maxValueNode(self, root):
        curr = root
        while curr and root.right:
            curr = curr.right
        return curr
# ========================================================================================================#
#                                    FIND SUM OF ALL NODES - O(N)
# ========================================================================================================#
    #  FIND SUM OF ALL NODES:
    def findSum(self, root):
        if root is None:
            return 0
        return root.value+self.findSum(root.left)+self.findSum(root.right)
# ========================================================================================================#
#                                       SEARCH NODES - O(LOG N)
# ========================================================================================================#
    # SEARCH O(log n) time.
    def search(self, root,target):
        # no tree
        if not root:
            return False
        if target > root.value:
            return self.search(root.right, target)
        elif target < root.value:
            return self.search(root.left, target)
        else: 
            return True
# ========================================================================================================#
#                                       VERIFY BST - O(N)
# ========================================================================================================#

def is_bst(node, left=float('-inf'), right=float('inf')):
    # An empty tree is a valid BST
    if not node:
        return True

    # Check if node val is greater than its left and lower than its right
    if not (left < node.val < right):
        return False

    # Recursively check the left and right subtrees with updated ranges
    return (is_bst(node.left, left, node.val) and
            is_bst(node.right, node.val, right))
# ========================================================================================================#
#                                       HEIGHT OF BST - O(N)
# ========================================================================================================#

def height(self, node):
    if node is None:
        return -1  # Returning -1 because height of an empty tree is -1
    else:
        # Compute the height of each subtree
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        # Use the larger one
        return max(left_height, right_height) + 1

# Assign root to the Tree
tree = Tree()
tree.root = root

# Get the height of the tree
tree_height = height(tree.root)
print("Height of the tree:", tree_height)



# ========================================================================================================#
#                                      
# ========================================================================================================#
arr = [1,4,3,7,4,9]
# root = TreeNode(3)
# print(root.value)
def createTree(arr, r):
    root= TreeNode(r)
    for n in arr:
        root.insert(root, n)
    return root


example= createTree(arr, 3)

# from dsa import pretty_print
# print(createTree(arr, 3))
print(example.search(example, 10))
