class Solution:
    def climbStairs(self, n: int) -> int:
        # subproblem: what are the amount of ways to reach the ith step in the staircase
        dp = [0] * (n+1)
        # base case
        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
