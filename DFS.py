from collections import deque

def dfs(graph,node,visited = set()):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph,neighbor,visited)
        
        
        
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': [],
}

start = 'A'

dfs(graph,start)


