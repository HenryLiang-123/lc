class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        
        for dst, src in prerequisites:
            adj_list[src].append(dst)

        t_sort = []
        def dfs(node, path): # true = can continue, false = cycle = invalid

            if node in seen:
                return True

            if node in path:
                return False

            path.add(node)
            for nei in adj_list[node]:
                if not dfs(nei, path):
                    return False

            path.remove(node)
            seen.add(node)
            t_sort.append(node)

            return True
        seen = set()

        for i in range(numCourses):
            if i not in seen:
                if not dfs(i, set()):
                    return []
                
        return t_sort[::-1]