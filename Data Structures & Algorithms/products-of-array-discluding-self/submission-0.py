class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # utilize prefix and suffix multiplicative arrays to solve problem optimally
        suffix = [1] * len(nums)
        prefix = [1] * len(nums)

        suffix_num = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = suffix_num
            suffix_num *= nums[i]

        prefix_num = 1
        for i in range(len(nums)):
            prefix[i] = prefix_num
            prefix_num *= nums[i]

        res = []
        for i in range(len(nums)):
            res.append(suffix[i] * prefix[i])

        return res
        

            