class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array first to prevent duplicates
        # loop through every index, when we reach an indexed value
        # look at all future values and run a 2sum algorithm on it to see if matches constraint
        nums.sort()
        res = []

        for i,n in enumerate(nums):
            # base case
            if i > 0 and nums[i] == nums[i-1]:
                continue

            curr = nums[i]
            l,r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == -curr:
                    if [curr, nums[l], nums[r]] not in res:
                        res.append([curr, nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < -curr:
                    l += 1
                elif nums[l] + nums[r] > -curr:
                    r -= 1

        return res
            

