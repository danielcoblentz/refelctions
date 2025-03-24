# matrix = [  [0, 1, 1, 1, 1, 0, 0]
#             [1, 0, 0, 0, 1, 0, 0]
#             [1, 0, 0, 1, 0, 1, 0]
#             [1, 0, 1, 0, 0, 0, 0]
#             [1, 1, 0, 0, 0, 1, 1]
#             [0, 0, 1, 0, 1, 0, 1]
#             [0, 0, 0, 0, 1, 1, 0]]

def dfs(graph, start, visited=None):
    """
    Performs Depth-First Search on a graph.

    Args:
        graph: An adjacency list representing the graph (dictionary).
        start: The starting vertex for DFS.
        visited: A set to keep track of visited vertices (optional).

    Returns:
        A set of visited vertices.
    """
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# Example graph
graph = {
    'A': ['B', 'C', 'E', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F', 'D'],
    'D': ['C', 'A'],
    'E': ['A', 'B', 'F', 'G'],
    'F': ['C', 'E', 'G'],
    'G': ['E', 'F']
}

# Start DFS from vertex 'A'
print("DFS traversal:")
visited_nodes = dfs(graph, 'A')
print("\nVisited nodes:", visited_nodes)

