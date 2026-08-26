class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, combination):
            # stopping conditions
            if len(combination) == k:
                res.append(combination.copy())
                return
            if i > n:
                return
            
            # backtracking algo
            combination.append(i)
            dfs(i+1, combination)
            combination.pop()
            dfs(i+1, combination)
        
        dfs(1, [])
        return res
                
