class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # graph question, use bfs approach to find indegrees of the nodes 
        # store indegree of each node, which means the number of nodes that point directly to a given node, so the # of courses that are prerequisites of a given num course
        in_degree = {i:0 for i in range(numCourses)}
        # adjacency list stores all the nodes that a given node points to
        adj = defaultdict(set)
        is_pre_req = defaultdict(set)

        for pre, course in prerequisites:
            adj[pre].add(course)
            in_degree[course] += 1

        # Queue all nodes with 0 in-degree, this is our starting point for the prereqs
        queue = deque([crs for crs in in_degree if in_degree[crs] == 0])
        while queue:
            curr = queue.popleft()
            # all the nodes that our starting course points to
            for neighbor in adj[curr]:
                is_pre_req[neighbor].add(curr)
                is_pre_req[neighbor].update(is_pre_req[curr])
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        res = []
        for u,v in queries:
            if u in is_pre_req[v]:
                res.append(True)
            else:
                res.append(False)

        return res

        

        