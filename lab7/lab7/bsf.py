graph = { 
  '5': ['2', '3'], 
  '3': ['4', '3'], 
  '7': ['7'], 
  '2': [], 
  '4': ['7'], 
  '8': [] 
} 

visited = []  
queue = []    

# Function for BFS
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:  
        m = queue.pop(0) 
        print(m, end=" ")  
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(visited, graph, '5')  # Function calling
