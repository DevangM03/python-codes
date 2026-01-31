def dfs(node, graph, visited):
    if node in visited:
        return
    
    print(node)            # visit the node
    visited.add(node)      # mark as visited
    
    for neighbor in graph[node]:   # go deeper
        dfs(neighbor, graph, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = set()
dfs('A', graph, visited)

