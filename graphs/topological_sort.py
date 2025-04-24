adjacency_list = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['E'],
    'E': []
}

def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)

        # Sort neighbors in descending order (largest first)
        for neighbor in sorted(graph[node], reverse=True):
            dfs(neighbor)

        stack.append(node)

    # Sort keys to always start DFS with the largest available node
    for node in sorted(graph.keys(), reverse=True):
        if node not in visited:
            dfs(node)

    stack.reverse()
    return stack

if __name__ == '__main__':
    print(topological_sort(adjacency_list))
