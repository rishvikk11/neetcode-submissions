class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for r in range(rows):
            for c in range(cols):
                # base cases
                if grid[r][c] == "0" or grid[r][c] == "-1":
                    continue

                queue = deque([(r,c)])

                while queue:
                    coord_r, coord_c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = coord_r + dr, coord_c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                            queue.append((nr, nc))
                            grid[nr][nc] = "-1"

                num_islands += 1

        return num_islands


