class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        # since we can't rob first and last house, we do two separate robbing dp processes: first house to second to last house, and second house to last house
        # take the maximum between the two
        return max(self.capture(nums[1:]), self.capture(nums[:n-1]))

    def capture(self, nums):
        n = len(nums)
        dp = [0] * (n+1)
        # base cases
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])

        return dp[n]