class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj_list = defaultdict(list)

        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        def dfs(node, parent, path):
            if node in seen:
                # we're good
                return True

            if node in path:
                # cycle
                return False

            path.add(node)
            for nei in adj_list[node]:
                if nei != parent:
                    if not dfs(nei, node, path):
                        return False

            path.remove(node)
            seen.add(node)
            return True

        seen = set()
        result = dfs(0, 0, set())

        if not result or len(seen) != n:
            return False

        return True