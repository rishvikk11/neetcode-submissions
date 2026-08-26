class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search from k = 1 to max number of bananas you have in one pile to see what's the min k you can have to eat bananas in less than h hours
        l,r = 1, max(piles)
        min_k = float('inf')
        while l <= r:
            mid = (l+r) // 2
            hrs = 0
            for p in piles:
                if p <= mid:
                    hrs += 1
                else:
                    hrs += (-(p // -mid))
            if hrs <= h:
                min_k = min(min_k, mid)
                r = mid-1
            else:
                l = mid+1
        
        return min_k
        