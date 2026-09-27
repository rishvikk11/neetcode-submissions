class UnionFind:
    def __init__(self, nums):
        self.parent = [i for i in range(len(nums))]
        self.rank = [0] * len(nums)

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA == rootB:
            return False
        
        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootB] < self.rank[rootA]:
            self.parent[rootB] = rootA
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # extract all edge weights by creating an adjacency list
        # as we're calculating edge weights, we add it to a minheap
        # once our minheap is fully established and done adding all edge weights
        # we can start popping from the minheap, guaranteed to find minimum edge weights first
        # if an edge we pop creates a cycle in our current attempt of an mst
        # we must continue and not use that edge
        adj = defaultdict(list)
        edge_heap = []
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                edge_weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([j, edge_weight])
                adj[j].append([i, edge_weight])
                heapq.heappush(edge_heap, (edge_weight, i, j))

        min_cost = 0
        uf = UnionFind(points)
        while edge_heap:
            edge_weight, point_i, point_j = heapq.heappop(edge_heap)
            if uf.union(point_i, point_j):
                min_cost += edge_weight
        
        return min_cost
        