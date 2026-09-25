class UnionFind:
    def __init__(self, nums):
        self.parent = {num: num for num in nums}
        self.rank = {num: 1 for num in nums}
        self.max_size = 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA == rootB:
            return

        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
            self.rank[rootB] += self.rank[rootA]
            self.max_size = max(self.max_size, self.rank[rootB])
            print("Yippeee")
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += self.rank[rootB]
            self.max_size = max(self.max_size, self.rank[rootA])
            print("Hoorayyy")

        return


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nodes = set(nums)
        uf = UnionFind(nums)

        for num in nodes:
            if num + 1 in nodes:
                uf.union(num, num+1)

        return uf.max_size

