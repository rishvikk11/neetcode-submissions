class Solution:
    def climbStairs(self, n: int) -> int:
        # subproblem: what are the amount of ways to reach the ith step in the staircase
        dp = [0] * (n+1)
        # base case
        first, second = 1, 1

        for i in range(2, n+1):
            temp = second
            second += first
            first = temp

        return second
