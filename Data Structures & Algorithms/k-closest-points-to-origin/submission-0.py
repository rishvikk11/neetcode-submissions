class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(self.distance(p), p) for p in points]
        heapq.heapify(distances)

        res = []
        for i in range(k):
            res.append(heapq.heappop(distances)[1])

        return res


    def distance(self, p):
        x,y = p[0], p[1]
        return math.sqrt(x ** 2 + y ** 2)