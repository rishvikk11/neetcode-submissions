class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search approach: we have l, mid, and r, and two regions that are sorted separately given that nums is rotated weirdly
        # if nums[r] > nums[mid], then mid and r are in the same sorted region, and if nums[mid] > nums[l], then mid and l are in the same sorted region
        # if nums[mid] != min(nums), and the right region is sorted, then the min number has to be the left; if the left region is sorted, then the min number has to be to the right
        l,r = 0, len(nums)-1
        min_num = nums[0]

        while l <= r:
            # check if our current region is sorted and if yes, the first number of the cut must be the minimum
            if nums[l] < nums[r]:
                min_num = min(min_num, nums[l])
                break
            
            mid = (l+r) // 2
            min_num = min(min_num, nums[mid])
            # left side sorted
            if nums[mid] >= nums[l]:
                l = mid+1
            # right side sorted
            else:
                r = mid-1
        return min_num

