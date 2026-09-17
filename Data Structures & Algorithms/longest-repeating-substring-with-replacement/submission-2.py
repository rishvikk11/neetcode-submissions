class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # stopping condition is window_len - most freq. character in the window > k
        l = 0
        max_window = -1
        # key = char, value = count of char in current window
        counts = {}

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            while (r-l+1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            max_window = max(max_window, r-l+1)
        
        return max_window