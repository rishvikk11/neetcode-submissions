class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        paths = set()

        def dfs(r, c, length):
            # base cases
            if length == len(word):
                return True
            if not (0 <= r < rows) or not (0 <= c < cols) or word[length] != board[r][c] or (r,c) in paths:
                return False

            paths.add((r, c))
            res = (
                dfs(r + 1, c, length + 1)
                or dfs(r - 1, c, length + 1)
                or dfs(r, c + 1, length + 1)
                or dfs(r, c - 1, length + 1)
            )
            paths.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
