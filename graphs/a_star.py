import heapq

def a_star(graph, start, goal, heuristic):
    """
    A* search algorithm.

    graph: dict of {node: [(neighbor, weight)]}
    heuristic: dict of {node: estimated cost to goal}
    """
    open_set = [(0 + heuristic[start], 0, start, [])]  # (f, g, node, path)

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        path = path + [current]

        if current == goal:
            return path, g  # Return path and total cost

        for neighbor, cost in graph[current]:
            heapq.heappush(open_set, (g + cost + heuristic[neighbor], g + cost, neighbor, path))

    return None, float('inf')  # No path

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}
heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 0}

path, cost = a_star(graph, 'A', 'D', heuristic)
print("A* Path:", path)
print("Total cost:", cost)
