class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        for prereq in prerequisites:
            prereqs[prereq[0]].append(prereq[1])
        having = set()
        done = set()
        result = []
        def dfs(course):
            if course in done:
                return True
            if course in having:
                return False
            having.add(course)
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
            result.append(course)
            done.add(course)
            return True
        for course in  range(numCourses):
            if not dfs(course):
                return []
        return result
            
