class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # same as course schedule 1, but topo order is an array instead of a counter this time and return topo order
        adj = defaultdict(list)
        in_degree = {i:0 for i in range(numCourses)}

        for u,v in prerequisites:
            adj[u].append(v)
            in_degree[v] += 1

        queue = deque([i for i, in_deg in in_degree.items() if in_deg == 0])
        topo_order = []

        while queue:
            course = queue.popleft()
            topo_order.append(course)

            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) != numCourses:
            return []
        return topo_order[::-1]