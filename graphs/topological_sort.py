from collections import deque, defaultdict

def topological_sort(graph):
    """
    Performs topological sort using Kahn's Algorithm (BFS-based).

    Args:
        graph: A dictionary representing a directed graph, 
               where keys are nodes and values are lists of neighbors.

    Returns:
        A list representing the topological order if valid, 
        or None if a cycle is detected.
    """
    in_degree = defaultdict(int)

    # Calculate in-degrees
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Nodes with 0 in-degree
    queue = deque([node for node in graph if in_degree[node] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If topo_order doesn't contain all nodes there was a cycle
    if len(topo_order) != len(graph):
        return None
    return topo_order

# example DAG
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}

# Run topological sort
result = topological_sort(graph)

if result:
    print("Topological Sort Order:", result)
else:
    print("The graph has a cycle. Topological sort not possible.")
