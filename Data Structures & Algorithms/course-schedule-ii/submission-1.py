class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]

        for a,b in prerequisites:
            adj[a].append(b)
            indegree[b] += 1

        queue = deque([i for i, crs in enumerate(indegree) if crs == 0])
        topo_ordering = []

        while queue:
            course = queue.popleft()
            topo_ordering.append(course)            

            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_ordering) < numCourses:
            return []
        return topo_ordering[::-1]