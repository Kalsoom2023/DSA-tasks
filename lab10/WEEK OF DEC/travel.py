import heapq
class Graph:
    def __init__(self):
        self.graph = {}

    def add_location(self, location):
        """Add a node (location) to the graph."""
        if location not in self.graph:
            self.graph[location] = {}

    def add_route(self, source, destination, weight):
        """Add a weighted edge (route) between two locations."""
        self.add_location(source)
        self.add_location(destination)
        self.graph[source][destination] = weight
        self.graph[destination][source] = weight  # Undirected graph

    def display_graph(self):
        """Display the graph structure."""
        for location, routes in self.graph.items():
            print(f"{location} -> {routes}")
def dijkstra(graph, start, end):
    """
    Find the shortest path between two nodes using Dijkstra's algorithm.
    """
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # (cost, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruct the shortest path
    path = []
    while end:
        path.append(end)
        end = previous_nodes[end]
    path.reverse()

    return distances[path[-1]], path
if __name__ == "__main__":
    # Create the graph
    travel_graph = Graph()

    # Add locations and routes
    travel_graph.add_route("A", "B", 5)
    travel_graph.add_route("A", "C", 10)
    travel_graph.add_route("B", "C", 3)
    travel_graph.add_route("B", "D", 9)
    travel_graph.add_route("C", "D", 2)

    print("Graph Structure:")
    travel_graph.display_graph()

    # User inputs
    print("\n--- Travel Planner ---")
    start_location = input("Enter the starting location: ").strip()
    end_location = input("Enter the destination location: ").strip()

    if start_location in travel_graph.graph and end_location in travel_graph.graph:
        distance, route = dijkstra(travel_graph.graph, start_location, end_location)
        print(f"\nShortest Route from {start_location} to {end_location}:")
        print(f"Distance: {distance}")
        print(f"Route: {' -> '.join(route)}")
    else:
        print("Invalid locations entered. Please try again.")
