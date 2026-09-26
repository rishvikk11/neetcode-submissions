class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(start, curr_comb):
            # base cases
            if len(curr_comb) == k:
                res.append(curr_comb.copy())
                return
            if start > n+1:
                return
            
            for i in range(start, n+1):
                curr_comb.append(i)
                dfs(i+1, curr_comb)
                curr_comb.pop()

        dfs(1, [])

        return res
