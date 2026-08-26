class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # initalize your data structure + variables
        mapping = {}
        res = 0

        for n in nums:
            if n not in mapping: # only wanna update new numbers
                left = mapping.get(n-1, 0)
                right = mapping.get(n+1, 0)
                
                length = left + right + 1
                mapping[n] = length
                
                # update left and right boundaries
                mapping[n-left] = length
                mapping[n+right] = length

                res = max(res, length)
        
        return res