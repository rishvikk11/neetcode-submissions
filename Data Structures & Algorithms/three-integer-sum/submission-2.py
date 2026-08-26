class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # the idea with this question is that we must do a two pointer approach while looping through each possibility
        # sort the numbers first and skip duplicates if we see the same starting number again
        sorted_nums = sorted(nums)
        print(sorted_nums)
        res = []
        for i in range(len(sorted_nums)):
            if sorted_nums[i] > 0:
                break
            l = i+1
            r = len(sorted_nums)-1
            # checking for duplicates and avoiding them
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            while l < r:
                if sorted_nums[i]+sorted_nums[l]+sorted_nums[r] > 0:
                    r -= 1
                elif sorted_nums[i]+sorted_nums[l]+sorted_nums[r] < 0:
                    l += 1
                else:
                    if [sorted_nums[i],sorted_nums[l],sorted_nums[r]] not in res:
                        res.append([sorted_nums[i],sorted_nums[l],sorted_nums[r]])
                    l += 1
                    r -= 1

        return res

            

