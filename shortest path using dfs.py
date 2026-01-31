graph = {
    "Lucknow": ["Kanpur", "Varanasi"],
    "Kanpur": ["Lucknow", "Agra"],
    "Varanasi": ["Lucknow", "Prayagraj"],
    "Prayagraj": ["Varanasi", "Delhi"],
    "Agra": ["Kanpur", "Delhi"],
    "Delhi": ["Agra", "Prayagraj"]
}

def dfs(graph, current, goal, visited, path, shortest):
    if current == goal:
        if not shortest or len(path) < len(shortest[0]):
            shortest.clear()
            shortest.append(path[:])
        return

    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            dfs(graph, neighbor, goal, visited, path + [neighbor], shortest)
            visited.remove(neighbor)

shortest = []

dfs(graph, "Lucknow", "Delhi", {"Lucknow"}, ["Lucknow"], shortest)

print("Shortest Path:", shortest[0])
