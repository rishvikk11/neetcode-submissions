class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # k is our starting node
        # we have to see what is the minimum distance from node k to every other node in the graph (dijkstra's algorithm)
        # run dijkstra's algorithm to find minimum distances and then take the max of those minimum distances to find the minimum time to reach ALL n nodes

        # create an adjacency list for each node and distances array
        distances = {node: float('inf') for node in range(1, n+1)}
        distances[k] = 0
        adj = defaultdict(list)

        for start, dest, weight in times:
            adj[start].append([dest, weight])

        # create a min heap storing our source node which is k 
        # every element pushing onto the min heap needs to be (the distance from k to the node, node)
        # we use a min heap so we can access the lowest edge weights of our neighbors first
        min_heap = []
        heapq.heappush(min_heap, (0, k))

        # pop the node we need to explore and look at its neighbors
        while min_heap:
            k_to_node, node = heapq.heappop(min_heap)
            # check if this distance is larger than its current distance from k
            # skip if it is because we already found a shorter path to it
            if k_to_node > distances[node]:
                continue

            # explore all neighbors and add to heap
            for neighbor, neighbor_weight in adj[node]:
                k_to_neighnode = k_to_node + neighbor_weight

                # intuitively, update distances but also only push heap if we found a shorter path, otherwise it's useless cuz we already traversed a path with lower cost
                if k_to_neighnode < distances[neighbor]:
                    distances[neighbor] = k_to_neighnode
                    heapq.heappush(min_heap, (k_to_node + neighbor_weight, neighbor))

        # traverse all the distances; if there is a float('inf'), return -1, if there isn't, take the maximum of the distances
        min_time = -1
        for node, dist in distances.items():
            if dist == float('inf'):
                return -1
            min_time = max(min_time, dist)

        return min_time
