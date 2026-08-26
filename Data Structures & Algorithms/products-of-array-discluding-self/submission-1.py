class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [0] * len(nums)
        prefix = [0] * len(nums)

        # calculating suffixes
        suffix_value = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = suffix_value
            suffix_value *= nums[i]
        
        # calculating prefixes
        prefix_value = 1
        for i in range(len(nums)):
            prefix[i] = prefix_value
            prefix_value *= nums[i]
        
        res = [0] * len(nums)
        for i in range(len(res)):
            res[i] = suffix[i] * prefix[i]
        
        return res
