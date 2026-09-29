class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # start at index (0,0) with a visited array
        # run a bfs routine to find unvisited ones within ur up, down, left, right directions
        # once we reach the bottom right index, we know to stop

        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(rows):
            for c in range(cols):
                # -1 represents a visited cell
                if grid[r][c] == "0" or grid[r][c] == "-1":
                    continue

                # we know this coordinate is a 1 and since it's a 1, run a bfs routine to find all adjacent ones connecting it to make it an island
                queue = deque([(r,c)])
                while queue:
                    coord_r, coord_c = queue.popleft()
                    for dr,dc in directions:
                        nr, nc = coord_r+dr, coord_c+dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == "1":
                                queue.append((nr, nc))
                                grid[nr][nc] = "-1"

                islands += 1

        return islands
