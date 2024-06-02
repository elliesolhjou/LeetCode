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
    queue.append_right((0,0))
    # 4- add to visit to avoid duplicates
    visit.add((0,0))
    # 5- initiate length
    length = 0
    # 6- ITERATE 
    while queue:
        for i in range(len(queue)):
            # 7- grab each cell to perform conditions, base case and edge cases
            r,c = queue.pop_left()
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



# ========================================================================================================#
#                                      ADJACENCY LIST - DFS - FIND PATH 
# ========================================================================================================#
'''1. Write a depth first search function that accepts
a starting vertex and an ending vertex. 
If the ending vertex is found, It should also 
return the path of the search.
'''

def dfs(start, end, adjList, path = None, visit = None):
    if path is None:
        path = []
    if visit is None:
        visit = set()
    
    # base case
    if start == end:
        return path
    
    # start path
    path.append(start)
    # add visited Nodes
    visit.add(start)

    # now start recursive call for visited node neighbors(connections)
    for neighbor in adjList[start]:
        if neighbor not in visit:
            result = (dfs(neighbor, end, adjList, path.copy(), visit.copy()))
            if result is not None:
                return result
    
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_vertex = 'A'
end_vertex = 'F'
path = dfs(start_vertex, end_vertex, graph)
# print("Path from", start_vertex, "to", end_vertex, ":", path)
print(path)


# ========================================================================================================#
#                                      ADJACENCY MATRIX - BFS - FIND PATH 
# ========================================================================================================#
'''
2. Implement a breadth first search function that accepts a starting 
vertex and an ending vertex of a graph. This time, assume that the graph is 
implemented using an adjacency matrix.
'''
from collections import deque

def bfs(start, end, adj_matrix):
    num_vertices = len(adj_matrix)
    visited = [False] * num_vertices
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path

        visited[current] = True

        for neighbor in range(num_vertices):
            if adj_matrix[current][neighbor] == 1 and not visited[neighbor]:
                queue.append((neighbor, path + [neighbor]))
                visited[neighbor] = True

    return None


adj_matrix = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0]
]

start_vertex = 0  # Representing 'A'
end_vertex = 5    # Representing 'F'
path = bfs(start_vertex, end_vertex, adj_matrix)
print("Path from", start_vertex, "to", end_vertex, ":", path)
