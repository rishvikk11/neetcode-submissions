class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # we need to find a path from top left corner to bottom right corner with minimum elevation
        # this is a variant of dijkstra's as each edge weight in the path is the maximum possible height we've encountered so far in the path

        # we start with max height being the first top left node
        # initialize minheap with the first node in our matrix
        rows, cols = len(grid), len(grid[0])
        min_heap = [(grid[0][0], (0,0))] # (max height seen, current grid cell)
        # initialize a visited set to keep track of nodes we already visited
        visited = {(0,0)}
        # this ensures that we've already traveled to the shortest path to that node
        # handle base cases within while loop
        while min_heap:
            max_height, (r,c) = heapq.heappop(min_heap)

            if r == rows-1 and c == cols-1:
                return max_height

            for dr,dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    max_val = max(max_height, grid[nr][nc])
                    heapq.heappush(min_heap, (max_val, (nr, nc)))

        # then, we traverse every neighbor of our current grid cell
        # add each neighbor to our minheap, where the edge weight is the maximum of our current grid cell or the neighbor grid cell
        # once we encounter the bottom right corner, return the max edge value
