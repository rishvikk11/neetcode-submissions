class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # create an adjacency list connecting the prerequisites, where a course will point to another course if you need to take that other course before taking the current course
        # create an in_degree hash map of all the courses

        # loop through the queries, the course at the second index is your source node here
        # run a bfs routine to see if that second indexed course is connected to the first indexed course
        # if we find it, then return true, otherwise false

        adj = defaultdict(list)
        in_degree = {i:0 for i in range(numCourses)}
        prereqs = [set() for i in range(numCourses)]

        for u,v in prerequisites:
            adj[u].append(v)
            in_degree[v] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while queue:
            course = queue.popleft()
            
            for neighbor in adj[course]:
                prereqs[neighbor].add(course)
                prereqs[neighbor].update(prereqs[course])
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        res = [False] * len(queries)
        for i, (u,v) in enumerate(queries):
            if u in prereqs[v]:
                res[i] = True

        return res                
