class Graph:
    def __init__(self, vertices):
       self.adj = [[] for _ in range(vertices)]  

    def add_edge(self, s, t):
        self.adj[s].append(t)  
        self.adj[t].append(s) 

    def dfs_rec(self, visited, s):
        visited[s] = True 
        print(s, end=" ") 
        for i in self.adj[s]:
            if not visited[i]:
                self.dfs_rec(visited, i)

    def dfs(self):
        visited = [False] * len(self.adj) 

        for i in range(len(self.adj)):
            if not visited[i]:
                self.dfs_rec(visited, i)


if __name__ == "__main__":
    V = 6  
    graph = Graph(V)
    edges = [(1, 2), (3, 0), (0, 2), (4, 5)]

    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    print("Complete DFS of the graph:")
    graph.dfs()  
