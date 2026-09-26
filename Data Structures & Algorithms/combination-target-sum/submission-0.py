class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, curr_sum):
            if sum(curr_sum) > target:
                return
            if sum(curr_sum) == target:
                res.append(curr_sum.copy())
                return
            if i > len(nums):
                return

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue

                curr_sum.append(nums[j])
                dfs(j, curr_sum)
                curr_sum.pop()

        dfs(0, [])
        return res

            