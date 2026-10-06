class Solution:
    def longestPalindrome(self, s: str) -> str:
        # subproblem: dp[i][j] = longest palindrome from index i to index j
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_len, res_idx = 0, 0

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        res_idx = i
        
        return s[res_idx: res_idx + max_len]

