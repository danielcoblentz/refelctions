from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    bfs_order = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            bfs_order.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return bfs_order

# sample graph
graph = {
    'A': ['B', 'C', 'E', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F', 'D'],
    'D': ['C', 'A'],
    'E': ['A', 'B', 'F', 'G'],
    'F': ['C', 'E', 'G'],
    'G': ['E', 'F']
}

# Start BFS from vertex 'A'
print("BFS traversal:")
bfs_result = bfs(graph, 'A')
print("\nVisited nodes in BFS order:", bfs_result)
