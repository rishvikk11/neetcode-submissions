class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # subproblem: dp[i][j] represents the longest common subsequence between the prefixes text1[0...i-1] and text2[0...j-1]

        dp = [[0] * (len(text1)+1) for _ in range(len(text2)+1)]

        for i in range(1, len(text2)+1):
            for j in range(1, len(text1)+1):
                # since we're tracking prefixes, we need to see if text2[i-1] and text1[j-1] match
                if text2[i - 1] == text1[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[len(text2)][len(text1)]

        