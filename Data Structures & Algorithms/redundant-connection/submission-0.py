class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union find algorithm
        # if we have two vertices in the same component and try to add an edge between them, then we know a cycle exists and can safely assume that edge can be our redundant connection to return
        n = len(edges)
        parent, rank = [0] * (n+1), [0] * (n+1)
        for i in range(n):
            parent[i] = i

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA, rootB = find(a), find(b)

            if rootA == rootB:
                return False
            if rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            elif rank[rootB] < rank[rootA]:
                parent[rootB] = rootA
            else:
                parent[rootB] = rootA
                rank[rootA] += 1
            
            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]

        