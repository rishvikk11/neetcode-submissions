class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        maxLen = 0
        for num in nums: 
            if num-1 not in setNums: 
                length = 1
                while num+length in setNums:
                    length += 1
                maxLen = max(maxLen, length)

        return maxLen
