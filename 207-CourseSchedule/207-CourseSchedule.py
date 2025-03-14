// Last updated: 3/14/2025, 5:59:55 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for dst, src in prerequisites:
            adj_list[src].append(dst)

        seen = set()
        def has_cycle(node, path):
            if node in seen:
                # we've processed this, and its good
                return False

            if node in path:
                return True

            path.add(node)
            for nei in adj_list[node]:
                if has_cycle(nei, path):
                    return True

            path.remove(node)
            seen.add(node)
            return False

        for i in range(numCourses):
            if i not in seen:
                if has_cycle(i, set()):
                    return False

        return True
