class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        n = len(edges)
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        # find start of cycle
        seen = set()
        def start_of_cycle(node, parent):
            if node in seen:
                return True, node

            seen.add(node)
            for nei in adj_list[node]:
                if nei != parent:
                    isCycle, start = start_of_cycle(nei, node)
                    if isCycle:
                        return True, start

            return False, node

        _, start = start_of_cycle(1,1)
        
        path = set()
        def dfs(node, parent):
            if node in path:
                return True

            path.add(node)
            for nei in adj_list[node]:
                if nei != parent:
                    isCycle = dfs(nei, node)
                    if isCycle:
                        return True

            path.remove(node)
            return False

        dfs(start, start)

        for src, dst in reversed(edges):
            if src in path and dst in path:
                return [src, dst]