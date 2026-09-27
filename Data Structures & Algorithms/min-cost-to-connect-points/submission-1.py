class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # find the shortest weighted path from one arbitrary node to all the other nodes in the graph such that there's no cycle
        # we need to construct a graph, where each point points to every other point on the graph with edge weights being the manhattan distance
        # start at the first point 
        # add every neighboring edge weight into a minimum heap
        # traverse to the point with the lowest manhattan distance
        # add whatever point we visited into a visited set to ensure we don't visit it again and add redundant edge weights
        # once we've visited all nodes, return the total weight of all the edges

        min_heap = [ [0, (points[0][0], points[0][1])] ] # [edge weight, point]
        min_cost = 0
        visited = set()

        while min_heap:
            edge_weight, (x,y) = heapq.heappop(min_heap)
            if (x,y) in visited: 
                continue
            visited.add((x,y))
            min_cost += edge_weight
            # base cases
            if len(visited) == len(points):
                return min_cost

            for pt in points:
                x1,y1 = pt
                if x == x1 and y == y1:
                    continue
                if (x1, y1) in visited:
                    continue

                man_dist = abs(x - x1) + abs(y - y1)
                heapq.heappush(min_heap, [man_dist, (x1, y1)])

            