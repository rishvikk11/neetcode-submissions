class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make your result array and hashmap (the hashmap stores index of each value in array)
        res = []
        mapping = {}
        # when looping through array, you find a pair by complement formula, and if you don't find the pair, store in the hashmap
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mapping: 
                res = [mapping[complement], i]
                break
            mapping[nums[i]] = i

        return res