# ========================================================================================================#
#                                      HEAP - O(LOG N) - Kth Largest Element
# ========================================================================================================#

'''
    - Priority Queues
    - UNDER TEH HOOD IT USES ARRAY WHICH ARR[0] IS TAKEN BY MACHINE AND HEAP STARTS AT ARR[1]
    - HEAP PURPOSE:
        *** FIND MIN AND MAX EASILY***
    - HEAP IS A COMPLETE BINARY SEARCH TREE DATA STRUCTURE
        - complete BST = Structutre property + order property
        - no hole in tree -> structure property
        - order property -> defines min and max heap
'''
'''
    leftChild = 2*i
    rightChild = (2*i)+1
    parent = i//2

'''
from dsa import heap
class Heap:
    def __init__(self):
        self.Heap = [0]
        
# ========================================================================================================#
#                                      MIN-HEAP Vs. MAX-HEAP O(1)
# ========================================================================================================#

'''
        IN MIN-HEAP -> ALL DESCENDANTS ARE GREATER THAN THEIR ANCESTORS
        ON BOTH SIDES AND EACH LEVEL
        Vs.
        IN MAX-HEAP -> ALL DESCENDANTS ARE SMALLER THAN THEIR ANCESTORS
        ON BOTH SIDES AND EACH LEVEL
'''
# ========================================================================================================#
#                                      HEAP - PUSH O(LOG N)
# ========================================================================================================#
class Heap:
    def __init__(self):
        self.heap = [0]
        
    def push(self, value):
        self.heap.append(value)
        # heap[0] is under the hood
        i = len(self.heap)-1

        # Perculating up to satisfy order property of HEAP
        # compare child nodes
        while i>1 and self.heap[i] <self.heap[i//2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2
# ========================================================================================================#
#                                      HEAP - POP - O(LOG N)
# ========================================================================================================#
'''
in poping at the end you need to return teh value of popped element
BUT ALSO YOU NEED CHECK STRUCTURE AND ORDER PROPERTIES ARE MET
'''

class Heap:
    def __init__(self):
        self.heap = [0]
    
    def pop(self):
        # empty heap
        if len(self.heap) == 1:
            return None
        # one element in heap
        if len(self.heap) == 2:
            return self.heap.pop()

        # HEAP IS QUEUE -> FIFO
        # POPPED ELEMENT
        res = self.heap[1]
        
        # Move last value to root
        self.heap[1] = self.heap.pop()
        i = 1

        # NOW CHECK STRUCTURE AND ORDER PROPERTY
        # *** STRUCTURE PROPERTY ALWAYS HAVE LEFT CHILD
        # Percolate down
        while 2 * i < len(self.heap):
            if (2 * i + 1 < len(self.heap) and 
            self.heap[2 * i + 1] < self.heap[2 * i] and 
            self.heap[i] > self.heap[2 * i + 1]):
                # Swap right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                # Swap left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return res
    
# ========================================================================================================#
#                                      HEAPIFY - O(N)
# ========================================================================================================#
'''
Recall that to build a binary search tree with n elements, the time complexity is O(n log n). If we build our heap of size 
n by pushing each element this would also run in O(n log n) time. But there is actually a more efficient algorithm known as Heapify, which allows us to perform this operation in 
O(n) time.
'''
'''
    leftChild = 2*i
    rightChild = (2*i)+1
    parent = i//2

'''
class Heap:
    def __init__(self):
        self.heap = [0]
        
    def heapify(self, arr):
        # 0-th position is moved to the end
        arr.append(arr[0])

        self.heap = arr
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            # Percolate down
            i = cur
            while 2 * i < len(self.heap):
                if (2 * i + 1 < len(self.heap) and 
                self.heap[2 * i + 1] < self.heap[2 * i] and 
                self.heap[i] > self.heap[2 * i + 1]):
                    # Swap right child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    # Swap left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
            cur -= 1
