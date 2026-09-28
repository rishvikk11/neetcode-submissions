class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create an adjacency list of all our courses from prerequisites
        # create an indegree hashset based off of our adjacency list
        # create a queue, queueing up elements of zero indegree
        # loop while the queue is non empty and create a topological order
        # if the length of our topological order is not our number of courses
        # we cant finish all courses, otherwise we're fine

        adj = defaultdict(list)
        in_degree = {i:0 for i in range(numCourses)}

        for u,v in prerequisites:
            adj[u].append(v)
            in_degree[v] += 1

        queue = deque([i for i, in_deg in in_degree.items() if in_deg == 0])
        topo_order = 0

        while queue:
            course = queue.popleft()
            topo_order += 1

            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return topo_order == numCourses