class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA == rootB:
            return False
        
        self.components -= 1
        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1
        return True

    def get_comps(self):
        return self.components

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a tree is just a graph with no cycles
        # cycle detection
        # union find algo or bfs algo, bunch of ways
        uf = UnionFind(n)

        for u,v in edges:
            if not uf.union(u,v):
                return False
        if uf.get_comps() > 1:
            return False
        return True
