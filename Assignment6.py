'''
1. Write a depth first search function that accepts
a starting vertex and an ending vertex. 
If the ending vertex is found, It should also 
return the path of the search.
'''
from collections import deque
def dfs(start, target, adjList, visit = None, path = None):
    if visit is None:
        visit = set()
    if path is None:
        path = []
    if start == target:
        # path.append(start)
        return path
    
    visit.add(start)
    path.append(start)

    for neighbor in adjList[start]:
            if neighbor not in visit:
                result = dfs(neighbor, target, adjList, visit.copy(), path.copy())
                if result is not None:
                    return result
            
    return None       

adjList = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start_vertex = 'A'
end_vertex = 'F'
print(dfs(start_vertex, end_vertex, adjList))




'''

2. Implement a breadth first search function that accepts a starting 
vertex and an ending vertex of a graph. This time, assume that the graph is 
implemented using an adjacency matrix.
'''





'''
3. Why does Djikstra's Algorithm NOT work for graphs with negative weights?

4. Write a function that accepts a directed acyclic graph (DAG) and a path. It should return whether the path is valid or not.

 
'''






















'''
Write a function that accepts a starting vertex 
in a graph and returns the count of all the other 
vertices it can reach. You may use either an adjacency 
list or adjacency matrix graph implementation.
'''

from collections import deque
def dfs(start, adjList, visit = None):
    if visit is None:
        visit = set()

    if len(adjList[start]) == 0:

        pass
    
    visit.add(start)
    print(visit, "visit before recursion")


    for neighbor in adjList[start]:
            if neighbor not in visit:
                result = dfs(neighbor, adjList, visit)
                print(visit, "visit after recursion")
                
            
    return len(visit)-1      

adjList = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['k',],
    'k': [],
    'M' : []
}
start_vertex = 'A'
print(dfs(start_vertex, adjList))




