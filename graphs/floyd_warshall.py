def floyd_warshall(graph, V):
    """
    graph: 2D list where graph[i][j] = weight from i to j, or float('inf') if no edge
    V: number of vertices
    """
    dist = [row[:] for row in graph]  # Deep copy of graph

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

# Example graph (adjacency matrix)
INF = float('inf')
graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

result = floyd_warshall(graph, 4)

print("Shortest distances between all pairs:")
for row in result:
    print(row)
