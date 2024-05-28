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
'''
from dsa import deque
def bfs(grid):
    # 1- get grid dimensions:
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    # 2- for any BFS queue is necessary -> tell us at which level we are at  
    queue = deque
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

            

