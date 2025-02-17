class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        memo = {}
        def dfs(node):
            if node in memo:
                return memo[node]

            if node in seen:
                memo[node] = False
                return False

            seen.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    memo[nei] = False
                    return False
            memo[node] = True
            return True
        n = len(graph)
        result = []
        for i in range(n):
            seen = set()
            if dfs(i):
                result.append(i)

        return result