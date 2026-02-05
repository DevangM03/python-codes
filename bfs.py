from collections import deque

def bfs(start, graph):
    visited = set()          # keeps track of visited nodes
    queue = deque([start])   # queue to explore nodes level by level

    while queue:
        node = queue.popleft()   # take the first node from queue
        
        if node not in visited:
            print(node)          # visit the node
            visited.add(node)    # mark it as visited
            
            for neighbor in graph[node]:   # add its neighbors
                queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

bfs('A', graph)
