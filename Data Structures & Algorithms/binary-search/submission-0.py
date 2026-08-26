class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        mid = (l+r) // 2

        if target not in nums:
            return -1

        while nums[mid] != target:
            if target > nums[mid]:
                l = mid+1
                mid = (l+r) // 2
            if target < nums[mid]:
                r = mid-1
                mid = (l+r) // 2
        
        return mid

