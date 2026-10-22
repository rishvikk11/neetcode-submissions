class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(open, close, st):
            # base case(s)
            if len(st) == 2*n:
                res.append(st)
                return

            if open < n:
                dfs(open+1, close, st+'(')
            if close < open:
                dfs(open, close+1, st+')')
            
        dfs(0,0,"")
        return res