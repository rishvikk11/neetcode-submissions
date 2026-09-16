class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMin, globMax = nums[0], nums[0]
        currMin, currMax = 0, 0
        total = 0

        # either normal kadane's or if max subset wraps around, subtract minimum subset sum from total

        for n in nums:
            currMax = max(n, currMax + n)
            currMin = min(n, currMin + n)
            total += n
            globMax = max(globMax, currMax)
            globMin = min(globMin, currMin)

        # total - globMin will always be 0 if all nums are negative
        return max(globMax, total-globMin) if globMax > 0 else globMax
        
