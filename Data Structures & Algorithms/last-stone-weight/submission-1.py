class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while stones:
            # base case
            if len(stones) == 1:
                return -stones[0]
            first, second = heapq.heappop(stones), heapq.heappop(stones)
            first, second = -first, -second
            if first > second:
                val = first-second
                heapq.heappush(stones, -val)

        return 0
