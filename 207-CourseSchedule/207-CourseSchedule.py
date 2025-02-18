from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for i in prerequisites:
            end = i[0]
            start = i[1]
            adj_list[start].append(end)

        seen = set()
        def dfs(course):
            if course in seen:
                return False
            if len(seen) == numCourses:
                return True
            seen.add(course)
            for nei in adj_list[course]:
                result = dfs(nei)
                if not result:
                    return False
                else:
                    adj_list[course] = []

            seen.remove(course)
            return True

        for i in list(adj_list.keys()):
            result = dfs(i)
            if not result:
                return False

        return True
        

