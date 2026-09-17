class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # dynamic sliding window solution, k not given, need to find a minimum subarray
        l, currSum = 0, 0
        min_window = float('inf')

        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target and l <= r:
                min_window = min(min_window, r-l+1)
                currSum -= nums[l]
                l += 1
            
        if min_window == float('inf'):
            return 0
        return min_window

            