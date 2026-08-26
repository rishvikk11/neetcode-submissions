class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        last_seen = {}
        max_len = 0
        l = 0
        for r,c in enumerate(s):
            if c in last_seen and last_seen[c] >= l:
                l = last_seen[c] + 1
            last_seen[c] = r
            max_len = max(max_len, r-l+1)
        return max_len
