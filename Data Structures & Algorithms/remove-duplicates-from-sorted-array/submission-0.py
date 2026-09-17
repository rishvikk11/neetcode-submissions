class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0 # will track where the next unique number needs to be placed

        for r in range(len(nums)):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
            
        return l+1