from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack=None, component=None):
        visited[v] = True
        if component is not None:
            component.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack, component)
        if stack is not None:
            stack.append(v)

    def get_transpose(self):
        g_transpose = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                g_transpose.add_edge(v, u)
        return g_transpose

    def kosaraju_scc(self):
        stack = []
        visited = [False] * self.V

        # 1st DFS: fill stack with finish times
        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        # Transpose the graph
        transposed = self.get_transpose()

        # 2nd DFS on transposed graph
        visited = [False] * self.V
        sccs = []

        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                transposed.dfs(v, visited, component=component)
                sccs.append(component)

        return sccs

# Example usage
g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 3)
g.add_edge(6, 5)
g.add_edge(6, 7)
g.add_edge(7, 6)

sccs = g.kosaraju_scc()

# Print strongly connected components
print("Strongly Connected Components:")
for comp in sccs:
    print(comp)
