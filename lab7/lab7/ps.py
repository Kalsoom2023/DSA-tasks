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
                    
    return []  
def if_dfs_path(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
        
    if start == goal:
        return True
    
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            if if_dfs_path(graph, neighbor, goal, visited):
                return True
                
    return False

def rescue_mission():
    n=int(input("Number of nodes: "))
    graph=defaultdict(list)
    for _ in range(n-1):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    start,person=map(int,input("Enter s and p position").split())
    hq=int(input("Enter hq position"))
    shortestpath=bfs_shortest_path(graph,start,person)
    if_dfs_path=if_dfs_path(graph,person,hq)
    print("Shortest path from start to person: ",shortestpath)
    print("Direct path from person to hq: " if if_dfs_path else "No")
    print("Total clearings: ",len(graph))
rescue_mission()
    
    