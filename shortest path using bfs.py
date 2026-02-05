from collections import deque

graph = {
    "Lucknow": ["Kanpur", "Varanasi"],   
    "Kanpur": ["Lucknow", "Agra"],       
    "Varanasi": ["Lucknow", "Prayagraj"],
    "Prayagraj": ["Varanasi", "Delhi"],  
    "Agra": ["Kanpur", "Delhi"],         
    "Delhi": ["Agra", "Prayagraj"]       
}

# this function will find the shortest path between two cities using BFS
def bfs_shortest_path(graph, start, goal):
    # create a queue to keep track of paths we are exploring
    # we start with a path that only has the starting city
    queue = deque([[start]])

    # keep exploring until there are no more paths left
    while queue:
        # take the first path from the queue
        path = queue.popleft()  # popleft() removes and returns the first item in the queue

        # the current city we are looking at is the last one in the path
        # if this city is the one we want (goal), then we found our path
        if path[-1] == goal:
            return path  

        # otherwise, look at all cities connected to the current city
        for neighbor in graph[path[-1]]:
            # if this connected city is not already in our path (to avoid going in circles)
            if neighbor not in path:
                # create a new path that adds this neighbor and put it in the queue
                queue.append(path + [neighbor])

# use the function to find the shortest path from Lucknow to Delhi
print("Shortest Path:", bfs_shortest_path(graph, "Lucknow", "Delhi"))



