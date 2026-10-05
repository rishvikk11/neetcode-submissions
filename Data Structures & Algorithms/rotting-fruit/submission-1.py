class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        fresh_oranges = 0

        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        if fresh_oranges == 0:
            return 0

        mins = 0
        while queue and fresh_oranges > 0:
            n = len(queue)
            mins += 1
            for _ in range(n):
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh_oranges -= 1

        return mins if fresh_oranges == 0 else -1
