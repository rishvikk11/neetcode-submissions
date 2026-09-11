class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # dfs approach, check when we start with a course v, if course u is in its path upwards, so in its prereq map
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)

        pre_req_map = {}

        # this dfs algo returns the prereq map of each course
        def dfs(course):
            if course not in pre_req_map:
                pre_req_map[course] = set()
                for prereq in adj[course]:
                    pre_req_map[course].update(dfs(prereq))
                pre_req_map[course].add(course)

            return pre_req_map[course]

        # updating prereq map of each course
        for i in range(numCourses):
            dfs(i)

        res = []
        for u,v in queries:
            if u in pre_req_map[v]:
                res.append(True)
            else:
                res.append(False)
        
        return res
            