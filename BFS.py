from collections import deque

def bfs(graph,start):
    visited = set()
    queue = deque([start])
    print(queue)
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            queue.extend(graph[node])
            
graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : [],
}

start = 'A'

bfs(graph,start)
        
    