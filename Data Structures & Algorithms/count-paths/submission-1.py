class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # subproblem: dp[i][j] = number of unique paths at coordinate (i,j)
        dp = [[0] * (n+1) for _ in range(m+1)]
        # base case
        dp[1][1] = 1        

        for r in range(1, m+1):
            for c in range(1, n+1):
                dp[r][c] += dp[r-1][c] + dp[r][c-1]

        return dp[m][n]
