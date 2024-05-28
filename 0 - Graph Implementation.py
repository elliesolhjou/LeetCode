# ========================================================================================================#
#                                      
# ========================================================================================================#


# ========================================================================================================#
#                                      MATRIX GRAPH 
# ========================================================================================================#
'''
    - Undirected Graph
    - 2D Arrays to display matrix 
    - Accessing nodes => grid[0][2]
    - 0 == Node(Vertices)
    - 1 == NO Node (blocked)
    - E <= V^2
'''
# ========================================================================================================#
#                                      ADJACENCY MATRIX - O(V^2)
# ========================================================================================================#
'''
    - Directed Graph
    - Rare to use
    - should be squared matrix/ grid
    - count(nodes) = number of rows/cols
    - 0 == NO Node
    - 1 == Edge(E)
    - max Edge = V^2
    - Edges direction : ROW -> COL
'''
# ========================================================================================================#
#                                      ADJACENCY LIST - O(V)
# ========================================================================================================#
'''
    - LinkedList
    - can be both directed and undirected
    - ***no outgoing edge from a node - no neighbor for that node***
'''
# GraphNode used for adjacency list
class GraphNode:
    def __init__(self, val):
        self.value = val
        self.neighbors = []

# ========================================================================================================#
#                                      MATRIX DFS - COUNT UNIQUE PATHS - O(4^N*M)
# ========================================================================================================#
'''
    QUESTION: 
        Count the unique paths from the top left to the bottom right. 
        A single path may only move along 0's and can't visit the same cell more 
        than once.

    - how many ways to go from [0][0] to [4][4]
    - backtracking(has many overlaps with DFS)
    - memory complexity = O(n*m)
        - bfs - queue - shortest path
        - dfs - backtracking - count of unique path
'''
# Matrix (2D Grid)
matrix = [[0,0,0,0],
          [1,1,0,0],
          [0,0,0,1],
          [0,1,0,0]]
visit = set()
# Count paths (backtracking)
def dfs(grid, r, c, visit):
    #  r, c pointers to cell location(works with index)
    # 1 - get dimensions of matrix
    ROWS, COLS = len(grid), len(grid[0])
    # 2 - define edge cases:
        #   2.1 - if r, c pointers get out of bound
        #   2.2 - already visited
        #   2.3 - blocked (==1)
    if min(r, c)< 0 or r==ROWS or c==COLS or (r,c) in visit or grid[r][c] ==1:
        return 0
    # 3 - define base case if we reach to destination
    if r== ROWS-1 and c == COLS-1:
        return 1
    # 4 - we are on right path but not reached the destination we need add to visit (for uniqueness) 
    visit.add(r,c)

    # 5- DEFINE/SET MOVES - one cell above = c+1 | one cell right = r+1 | ....
    count = 0
    count+=dfs(grid, r+1, c, visit)
    count+=dfs(grid, r-1, c, visit)
    count+=dfs(grid, r, c+1, visit)
    count+=dfs(grid, r, c-1, visit)

    # backtract to make cells available starting from grid[0][0]
    visit.remove(r,c)

    return count

    
# ========================================================================================================#
#                                      MATRIX BFS - FIND SHORTEST PATHS - O(N*M)
# ========================================================================================================#
'''
    QUESTION:
        Find the length of the shortest path from top left of the grid to the 
        bottom right.
        - returns length
        - bfs - queue - shortest path
        - dfs - backtracking - count of unique path
'''
# from dsa import deque
def bfs(grid):
    # 1- get grid dimensions:
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    # 2- for any BFS queue is necessary -> tell us at which level we are at  
    queue = Deque()
    # 3- initiate queue with starting point (first node)
    queue.append((0,0))
    # 4- add to visit to avoid duplicates
    visit.add((0,0))
    # 5- initiate length
    length = 0
    # 6- ITERATE 
    while queue:
        for i in range(len(queue)):
            # 7- grab each cell to perform conditions, base case and edge cases
            r,c = queue.popleft()
            # 8- base case: check if we reached to destination
            if r==ROWS-1 and c==COLS-1:
                return length
            # 9- DEFINE/SET MOVES (difference row, difference col)
            neighbors = [[0,1], [1,0],[0,-1],[-1,0]]
            # 10- MOVE
            for dr, dc in neighbors:
                # 11- define edge cases
                if min(dr+r, c+dc)<0 or r+dr == ROWS or c+dc == COLS or (r+dr, c+dc) in visit or grid[r+dr][c+dc]==1:
                    continue
                # 12- if none of above happened we are good
                    # keep moving by extending path
                queue.append((r+dr, c+dc))
                visit.add((r+dr, c+dc))
        
        length+=1
    return length

# ========================================================================================================#
#                                      ADJACENCY LIST 
# ========================================================================================================#
'''

    - TO CODE GRAPH WITH ADJACENCYLIST (how to use illustartion to code):
        - either graphNode
        - or hashmap (better)

'''
# graphNode Approach
class GraphNode:
    def __init__ (self, val):
        self.val = val
        self.neighbors = []

# HASHMAP APPROACH
adjList = { "A": [], "B": [] }

# HOW CODIFY A GRAPH PICTURE
# 1- manually define edges
# A is source Node B is destination Node
edges= [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
# 2- initiate hashmap
adjList={}
# 3- add all nodes to hashmap
for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    # 3-1 if node already exists
    adjList[src].append(dst)

# ========================================================================================================#
#                                      ADJACENCY LIST - DFS - COUNT UNIQUE PATH - O(N^V)
# ========================================================================================================#
'''
    QUESTION: 
        Count the unique paths from the top left to the bottom right. 
        A single path may only move along 0's and can't visit the same cell more 
        than once.

        - bfs - queue - shortest path
        - dfs - backtracking - count of unique path
'''
def dfs(node, target, adjList, visit):
    # 1- define edge and base cases
    if node in visit:
        return 0
    if node == target :
        return 1
    
    # not an edge case nor base case
    count = 0
    # 2- add starting node to visit
    visit.add(node)
    # 3- ITERATE
    for neighbor in adjList[node]:
        count+=dfs(neighbor, target, adjList, visit)
    
    # 4-backtrack 
    visit.remove(node)

    return count
# ========================================================================================================#
#                                      ADJACENCY LIST - BFS - SHORTEST PATH - O(V+E)
# ========================================================================================================#
'''
    BFS:
        - queue
        - while loop
        - append
        - shortest path


    DFS:
        - backtracking
        - recursion
        - count of unique path

'''
def bfs(node, target, adjList):
    length = 0
    visit= set()
    visit.add(node)
    queue = Deque()
    queue.append(node)

    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return length
            for neighbor in adjList[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
            length +=1

    return length



    





class Deque:
    def __init__(self):
        # define array
        self.items=[]
        # create size (count of index)
        self.size = 0
    def append_left(self, element):
        # create new array with new size (adding one element every time appending = increasing size) in cpu
        new_items = [None] * (self.size+1)
        # assign first left cell to the element
        new_items[0] = element
        # Copy the existing elements to the new array, starting from index 1
        # shifting rest of previous elements to right
        for i in range(1, self.size+1):
            new_items[i] = self.items[i-1]
        self.items = new_items
        self.size +=1
    def append_right(self, element):
        # growing array -> creating new array with new size
        new_items = [None] * (self.size+1)
        # assign last cell of array on right to element
        new_items[self.size] = element
        # Copy the existing elements to the new array, starting from index 0
        for i in range(self.size+1):
            new_items[i] = self.items[i]
        self.items= new_items
        self.size+=1
    
    # pop return element
    def pop_left(self): 
        # if queue is empty raise an error
        if not self.size == 0:
            raise IndexError("empty queue")
        # grab value of popped element
        element = self.items[0]
        # create new array with new size
        new_items= [None] * (self.size-1)
        # shift elements to right
        for i in range(1, self.size-1):
            new_items[i-1] = self.items[i]
        self.items = new_items
        self.size -=1
        return element

    def pop_right(self):
        # return value
        # if queue is empty
        if self.size == 0:
            raise IndexError("empty stack")
        # grab return value
        element = self.items[self.size-1]
        # create new array
        new_items = [None]* (self.size-1)
        # copy old array elements to new array
        for i in range(self.size-1):
            new_items[i] = self.items[i]
        
        new_items = self.items
        self.size -=1
        return element

    def peek_left(self):
        # return value
        # check size
        if self.size == 0:
            raise IndexError ("empty queue")
        element = self.items[0]
        return element
    
    def peek_right(self):
        if self.size == 0:
            raise IndexError ("empty queue")
        return self.items[self.size-1]

    def get_count(self):
        return self.size
    
    def __str__(self):
        return str(self.items[:self.size])
    