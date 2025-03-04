// Last updated: 3/4/2025, 11:29:02 AM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for dst, src in prerequisites:
            adj_list[src].append(dst)

        seen = set()
        def hasCycle(node, path):
            if node in path:
                return True

            if node in seen:
                return False

            path.add(node)
            
            for nei in adj_list[node]:
                if hasCycle(nei, path):
                    return True
            seen.add(node)
            path.remove(node)
            return False

        for i in range(numCourses):
            if i not in seen:
                path = set()
                if hasCycle(i, path):
                    return False

        return True

