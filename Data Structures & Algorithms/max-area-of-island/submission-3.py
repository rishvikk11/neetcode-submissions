class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # same as number of islands, but have to keep track of max island through some global variable
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        maxArea = 0
        # in the grid, 1 = land (not visited), 0 = water, -1 = land (visited)

        for r in range(rows):
            for c in range(cols):
                # base cases
                if grid[r][c] == 0:
                    continue
                if grid[r][c] == -1:
                    continue

                grid[r][c] = -1
                
                queue = deque([(r,c)])
                area = 0
                while queue:
                    coord_r, coord_c = queue.popleft()
                    area += 1
                    for dr,dc in directions:
                        nr, nc = coord_r+dr, coord_c+dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            queue.append((nr, nc))
                            grid[nr][nc] = -1 # mark as visited

                maxArea = max(maxArea, area)

        return maxArea

