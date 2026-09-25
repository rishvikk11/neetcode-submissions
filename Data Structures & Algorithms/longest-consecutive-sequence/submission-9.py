class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numsSet = set(nums)
        maxLen = 1

        for n in numsSet:
            if n-1 not in numsSet:
                length = 1
                while n+length in numsSet:
                    length += 1
                maxLen = max(maxLen, length)

        return maxLen