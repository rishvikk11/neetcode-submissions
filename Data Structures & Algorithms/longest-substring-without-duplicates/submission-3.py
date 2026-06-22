class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupeSet = set()
        maxLen = 0
        l = 0
        for i in range(len(s)):
            while s[i] in dupeSet: 
               dupeSet.remove(s[l])
               l += 1
            dupeSet.add(s[i])
            maxLen = max(maxLen, i+1-l)
        return maxLen

