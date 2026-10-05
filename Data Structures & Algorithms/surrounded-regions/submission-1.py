class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        # do a bfs to find all 0's connected to 0's on the border to mark them as non capturable (NC)
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows-1 or c == 0 or c == cols-1) and board[r][c] == "O":
                    queue.append((r,c))

        while queue:
            coord_r, coord_c = queue.popleft()
            board[coord_r][coord_c] = "NC"
            for dr, dc in directions:
                nr, nc = coord_r + dr, coord_c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "NC":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"

