class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent, rank = [0] * n, [0] * n
        for i in range(n):
            parent[i] = i

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA, rootB = find(a), find(b)
            if rootA == rootB:
                return

            if rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            elif rank[rootB] < rank[rootA]:
                parent[rootB] = rootA
            else:
                parent[rootB] = rootA
                rank[rootA] += 1

            return 

        for u,v in edges:
            union(u,v)
        
        components = 0
        for i in range(n):
            if find(i) == i:
                components += 1

        return components           
