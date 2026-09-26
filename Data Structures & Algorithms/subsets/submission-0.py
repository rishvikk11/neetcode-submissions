class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # dfs/backtracking question
        # easy way to think about this is that you have a root, it points to all integers at indices greater than the current index we're on
        # each unique integer points to the integer at the next index greater than it, so integers only point to integers down the line (this prevents duplicate subsets)
        # add each possible path to our result array
        res = []

        def dfs(i, curr_subset):
            if i > len(nums):
                return

            res.append(curr_subset.copy())
            
            for j in range(i, len(nums)):
                curr_subset.append(nums[j])
                dfs(j+1, curr_subset)
                curr_subset.pop()
        
        dfs(0, [])
        return res
