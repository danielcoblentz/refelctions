class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False  # Already connected
        # Union by rank
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        return True

def kruskal(vertices, edges):
    """
    Kruskal's Algorithm to find the Minimum Spanning Tree

    Args:
        vertices: List of nodes in the graph.
        edges: List of tuples (weight, node1, node2)

    Returns:
        mst: List of edges in the MST
        total_cost: Sum of all edge weights in the MST
    """
    ds = DisjointSet(vertices)
    mst = []
    total_cost = 0

    # Sort edges by weight
    edges.sort()

    for weight, u, v in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost

# Example graph
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    (2, 'A', 'B'),
    (3, 'A', 'C'),
    (1, 'B', 'C'),
    (1, 'B', 'D'),
    (4, 'C', 'D'),
    (5, 'C', 'E'),
    (1, 'D', 'E')
]

mst_edges, total = kruskal(vertices, edges)

#  results
print("Kruskal's MST edges:")
for u, v, w in mst_edges:
    print(f"{u} - {v} (weight {w})")
print("Total Cost of MST:", total)
