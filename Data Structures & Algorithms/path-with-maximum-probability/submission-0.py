class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # variant of dijkstra's algo question
        # we want to find the path from start node to end node with maximum product of probabilities
        # create an adjacency matrix so that we can travel to the neighboring nodes of every visited node
        # establish a maxheap to travel to the node with higher probability out of all neighbors
        # however, when deciding which node to travel to, the edge of the neighboring weights must multiply with the current edge weight that got us to our current node
        # and we must travel to the highest product yielded weighted edge

        adj = defaultdict(list)
        for i, (source, destination) in enumerate(edges):
            adj[source].append([destination, succProb[i]])
            adj[destination].append([source, succProb[i]])

        max_heap = [(0, start_node)] # (probability away from start node, node)
        visited = set()

        while max_heap:
            prob_from_node, node = heapq.heappop(max_heap)

            if node == end_node:
                return -prob_from_node
            if node in visited:
                continue

            for neighbor, prob_weight in adj[node]:
                if prob_from_node == 0:
                    new_prob_weight = prob_weight
                else:
                    new_prob_weight = prob_weight * -prob_from_node

                heapq.heappush(max_heap, (-new_prob_weight, neighbor))

            visited.add(node)

        return 0
                
