# Using a Python dictionary to act as an adjacency list
graph = { 
  'A': ['B', 'C'], 
  'B': ['D', 'E'], 
  'C': ['F'], 
  'D': [], 
  'E': ['F'], 
  'F': [] 
}

visited = set()  # Set to keep track of visited nodes of graph

# Function for Depth-First Search (DFS)
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")  # Print the current node
        visited.add(node)  # Mark the node as visited
        # Recur for all the neighbors
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, 'A')  # Starting the DFS from node 'A'
