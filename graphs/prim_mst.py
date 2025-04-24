import heapq

def prim(graph, start):
    """
    find the Minimum Spanning Tree (MST) of a weighted graph.

    Args:
        graph: Dictionary where each key is a node and the value is a list of (neighbor, weight) pairs
        start: The starting node for the MST

    Returns:
        mst: List of edges in the MST as (from_node, to_node, weight)
        total_cost: Total weight of the MST
    """
    visited = set()
    min_heap = [(0, start, None)]  # (weight, current_node, from_node)
    mst = []
    total_cost = 0

    while min_heap and len(visited) < len(graph):
        weight, node, from_node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            total_cost += weight
            if from_node is not None:
                mst.append((from_node, node, weight))
            for neighbor, edge_weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor, node))

    return mst, total_cost

#  weighted undirected graph
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4), ('E', 5)],
    'D': [('B', 1), ('C', 4), ('E', 1)],
    'E': [('C', 5), ('D', 1)]
}

#  Prim's algorithm starting from node 'A'
mst_edges, total = prim(graph, 'A')


print("Minimum Spanning Tree Edges:")
for u, v, w in mst_edges:
    print(f"{u} - {v} (weight {w})")
print("Total Cost of MST:", total)
