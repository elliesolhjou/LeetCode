'''
Write a function that accepts a starting vertex in a graph and returns the count of all the other vertices it can reach. You may use either an adjacency list or adjacency matrix graph implementation.
'''

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




