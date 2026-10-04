class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(ocean, nodes):
            queue = deque(nodes)

            while queue:
                coord_r, coord_c = queue.popleft()
                ocean[coord_r][coord_c] = True

                for dr,dc in directions:
                    nr, nc = coord_r + dr, coord_c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not ocean[nr][nc]:
                        if heights[nr][nc] >= heights[coord_r][coord_c]:
                            queue.append((nr, nc))

        pac_q, atl_q = [], []

        for c in range(cols):
            pac_q.append((0,c))
            atl_q.append((rows-1, c))
        
        for r in range(rows):
            pac_q.append((r,0))
            atl_q.append((r, cols-1))

        res = []

        bfs(pacific, pac_q)
        bfs(atlantic, atl_q)
        
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r,c])

        return res

