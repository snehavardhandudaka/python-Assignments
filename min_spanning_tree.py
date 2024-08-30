class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            self.parent[item] = self.find(self.parent[item])
            return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def kruskal(graph):
    edges = sorted(graph['edges'], key=lambda edge: edge[2])
    ds = DisjointSet(graph['vertices'])
    mst = []

    for edge in edges:
        u, v, weight = edge
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append(edge)

    return mst

# Example graph
graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E'],
    'edges': [
        ('A', 'B', 1),
        ('A', 'C', 3),
        ('B', 'C', 1),
        ('B', 'D', 6),
        ('C', 'D', 5),
        ('C', 'E', 4),
        ('D', 'E', 2)
    ]
}

print(kruskal(graph))
