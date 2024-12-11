class Graph:
    def __init__(self, vertices):
        # Adjacency list
        self.adj = [[] for _ in range(vertices)]  

    def add_edge(self, s, t):
        self.adj[s].append(t)  
        self.adj[t].append(s) 

    def dfs_rec(self, visited, s):
        visited[s] = True 
        print(s, end=" ") 

        # Recursively visit all adjacent vertices
        # that are not visited yet
        for i in self.adj[s]:
            if not visited[i]:
                self.dfs_rec(visited, i)

    def dfs(self):
        visited = [False] * len(self.adj) 

        # Loop through all vertices to handle disconnected
        # graph
        for i in range(len(self.adj)):
            if not visited[i]:
                  # Perform DFS from unvisited vertex
                self.dfs_rec(visited, i)


if __name__ == "__main__":
    V = 6  # Number of vertices
    graph = Graph(V)

    # Define the edges of the graph
    edges = [(1, 2), (2, 0), (0, 3), (4, 5)]

    # Populate the adjacency list with edges
    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    print("Complete DFS of the graph:")
    graph.dfs()  # Perform DFS
