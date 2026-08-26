class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find sorted and unsorted region, if target falls within sorted region, then we just do regular binary search
        # otherwise, we go to unsorted region, and repeat the process above until we find target
        l,r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1     
        return -1           