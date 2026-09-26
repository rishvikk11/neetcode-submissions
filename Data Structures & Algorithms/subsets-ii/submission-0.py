class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # same idea as subsets question
        res = []
        visited = set()

        def dfs(start, curr_subset):
            # base cases
            if start > len(nums):
                return
            if tuple(sorted(curr_subset)) in visited:
                return

            res.append(curr_subset.copy())
            visited.add(tuple(sorted(curr_subset.copy())))

            for i in range(start, len(nums)):
                curr_subset.append(nums[i])
                dfs(i+1, curr_subset)
                curr_subset.pop()

        dfs(0, [])
        return res
