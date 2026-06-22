class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            maxLen = 0
        else:
            maxLen = 1
        l,r = 0,1
        while l < r and r < len(s):
            if len(set(s[l:r+1])) == len(s[l:r+1]):
                length = r+1-l
                maxLen = max(length, maxLen)
            else:
                l += 1
            r += 1
        return maxLen

