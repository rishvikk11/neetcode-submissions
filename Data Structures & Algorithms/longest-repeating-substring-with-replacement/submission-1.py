class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # as you grow the window, you find the number of distinct characters in the window, the window_len - max freq. char. in window is the number of replacements you can make
        # if the number of replacements you can extend is less than k, extend the window until you reach k replacements
        # once you reach k replacements, you move the entire window to the right until our window reaches the end of the string
        l = 0
        max_len = 0
        count = {}
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            replace = (r-l+1) - max(count.values())
            while replace > k:
                count[s[l]] -= 1
                l += 1
                replace = (r-l+1) - max(count.values())
            max_len = max(max_len, r-l+1)

        return max_len
