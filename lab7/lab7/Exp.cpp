from collections import deque, defaultdict

def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, [start])])  
    visited = set()
    
    while queue:
        node, path = queue.popleft()
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
                    
    return []  # Return empty list if no path exists
