class UnionFind:
    def __init__(self, elements):
        # Each element is its own parent
        self.parent = {e: e for e in elements}
        self.rank = {e: 0 for e in elements}

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by rank
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in the same set

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Example usage
elements = ['A', 'B', 'C', 'D', 'E']
uf = UnionFind(elements)

uf.union('A', 'B')
uf.union('C', 'D')
uf.union('B', 'C')

print("Are A and D connected?", uf.connected('A', 'D'))  # True
print("Are A and E connected?", uf.connected('A', 'E'))  # False
