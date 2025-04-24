import heapq

# Directed graph with positive weights
graph = {
    'A': {'B': 10, 'C': 15},
    'B': {'F': 15, 'D': 12},
    'C': {'E': 10},
    'D': {'F':1, 'E': 2},
    'E': {},
    'F': {'E': 5}
}

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node].items():
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return dist

# Run the shortest path algorithm from node A
start = 'A'
shortest_paths = dijkstra(graph, start)

# Print total cost from A to each node
print(f"Shortest path costs from '{start}':")
for node, cost in shortest_paths.items():
    print(f"  {start} → {node}: {cost}")
