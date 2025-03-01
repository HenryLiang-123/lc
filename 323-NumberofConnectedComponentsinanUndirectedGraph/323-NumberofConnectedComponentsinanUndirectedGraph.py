from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        global_seen = set()
        def bfs(root):
            nonlocal global_seen
            seen = set()
            global_seen.add(root)
            seen.add(root)
            q = deque([root])

            while q:
                node = q.popleft()
                for nei in adj_list[node]:
                    if nei not in seen:
                        seen.add(nei)
                        global_seen.add(nei)
                        q.append(nei)

            return seen
        result = []
        for i in range(n):
            if i not in global_seen:
                result.append(bfs(i))

        return len(result)

        
            