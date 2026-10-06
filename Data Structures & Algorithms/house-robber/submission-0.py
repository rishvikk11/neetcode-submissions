class Solution:
    def rob(self, nums: List[int]) -> int:
        # subproblem: what is the max amount of money i will have if i rob or do not rob this house
        n = len(nums)
        dp = [0] * (n+1)

        # base cases
        dp[0] = 0
        dp[1] = nums[0]

        # 1-indexed
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])

        return dp[n]

        