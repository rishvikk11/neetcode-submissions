class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        max_stops = {node: -1 for node in range(n)} # max stops left from any node in graph to the destination node
        max_stops[src] = k+1

        for u, v, cost in flights:
            adj[u].append((v, cost))

        min_heap = [(0, src, k+1)] # current cost, node, k

        while min_heap:
            cost, flight, k_val = heapq.heappop(min_heap)
            # base cases
            if flight == dst:
                return cost

            max_stops[flight] = k_val
            
            if k_val > 0:
                for neighbor, price in adj[flight]:
                    if max_stops[neighbor] < k_val - 1:
                        total_cost = cost + price
                        heapq.heappush(min_heap, (total_cost, neighbor, k_val-1))

        return -1