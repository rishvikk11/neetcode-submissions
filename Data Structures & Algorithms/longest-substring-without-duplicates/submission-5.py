class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, max_len = 0, 0
        last_seen = {}

        for r,c in enumerate(s):
            # check if there's a duplicate in our current window
            if c in last_seen and last_seen[c] >= l:
                l = last_seen[c]+1

            last_seen[c] = r
            max_len = max(max_len, r-l+1)
        
        return max_len