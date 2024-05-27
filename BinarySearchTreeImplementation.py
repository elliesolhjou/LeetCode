class TreeNode:
    def __init__(self, value, left= None, right= None):
        self.value = value
        self.left = left
        self.right = right


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

    # DELETION A NODE - O(n)
    def delete(self, root, value):
        if not root:
            return None
        if value > root.value:
            root.right = self.delete(root.right, value)
        elif value< root.value:
            root.left = self.delete(root.left, value)
        # else:

        
    # FIND MIN VAL
    def minValueNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    # FIND MAX VAL
    def maxValueNode(self, root):
        curr = root
        while curr and root.right:
            curr = curr.right
        return curr

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
