class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        l = 0
        max_len = -1
        first_seen = {}
        
        for r, char in enumerate(s):
            if char in first_seen:
                idx = first_seen[char]
                max_len = max(max_len, (r-1) - (idx+1) + 1)
            else:
                first_seen[char] = r
                
        return max_len