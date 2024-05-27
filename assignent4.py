'''
Write a function to reverse the elements in a doubly linked list. Do not simply print it out. 
It must have the references correctly set in reversed order.
Also, write a print method this should help with debugging.
'''

def reverse(dll):
    current = dll.head
    while current:
        # Swap the next and prev pointers
        current.prev, current.next = current.next, current.prev
        # Move to the next node (which is actually the previous node due to the swap)
        current = current.prev

    # Swap the head and tail
    dll.head, dll.tail = dll.tail, dll.head


'''
Write a function that takes two linked list and outputs a union of these two linked lists. Make it as efficient as possible. You can assume that each list consists of unique numbers and are not necessarily sorted. Also, the order of the output is not significant.
For example: [2, 10, 5, 3, 4] and [4, 7, 8, 3, 11] has a union of [2, 10, 3, 4, 5, 7, 8, 11]
'''

class Node:
    def __init__(self, val, next= None):
        self.value = val
        self.next = next


def linkListMaker(arr):
    if not arr:
        return None
    head = Node(arr[0])
    # pointer
    current = head
    for val in arr[1:]:
        # create node
        current.next = Node(val)
        # move pointer
        current = current.next
    
    return head


def unionMaker(arr1, arr2):
    head1 = linkListMaker(arr1)
    head2 = linkListMaker(arr2)
    if not head1 and not head2:
        return None
    
    unique_nodes = set()
    current = head1
    while current:
        unique_nodes.add(current.value)
        current = current.next
    
    current = head2
    while current:
        unique_nodes.add(current.value)
        current = current.next

    unique_nodes = list(unique_nodes)

    return linkListMaker(unique_nodes)


def printLinkedList(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Test the function
list1 = [2, 10, 5, 3, 4]
list2 = [4, 7, 8, 3, 11]

union_list = unionMaker(list1, list2)
printLinkedList(union_list)



'''
Write the following binary search tree functions to:
Return the minimum value
Return the maximum value
Return the sum of all values

'''
class TreeNode:
    def __init__(self, value, left= None, right= None):
        self.value = value
        self.left = left
        self.right = right

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

    def findSum(self, root):
        if root is None:
            return 0
        return root.value+self.findSum(root.left)+self.findSum(root.right)
    

'''
Write a function that accepts a binary tree and verifies whether it fulfills binary search tree conditions.
'''
