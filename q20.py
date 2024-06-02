'''

Write a function that accepts a valid binary heap and verifies whether it is a max-heap. '''


def validHeapMax(root): 
    def dfs(node): 
        if not node: 
            return True 
        if node.left: 
            if node.left.value > node.value: 
                return False 
        if node.right: 
            if node.right.value > node.value: 
                return False 
        left_valid = dfs(node.left) 
        right_valid = dfs(node.right) 
        return left_valid and right_valid 
    
    return dfs(root)