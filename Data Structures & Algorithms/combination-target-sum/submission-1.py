class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, curr, total_sum):
            if total_sum > target:
                return
            if total_sum == target:
                res.append(curr.copy())
                return
            if i > len(nums):
                return

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue

                curr.append(nums[j])
                dfs(j, curr, total_sum + nums[j])
                curr.pop()

        dfs(0, [], 0)
        return res

            