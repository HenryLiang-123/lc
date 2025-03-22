// Last updated: 3/22/2025, 12:47:26 PM
from collections import deque
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # each node needs k-1 neighbors, where k is the number of nodes in the component
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        global_seen = set()
        def bfs(node):
            q = deque([node])
            global_seen.add(node)
            curr_seen = set()
            curr_seen.add(node)
            while q:
                node = q.popleft()
                for nei in adj_list[node]:
                    if nei not in curr_seen:
                        curr_seen.add(nei)
                        global_seen.add(nei)
                        q.append(nei)

            return curr_seen
        result = 0
        for i in range(n):
            if i not in global_seen:
                curr_component = bfs(i)
                if all([len(adj_list[node]) == len(curr_component) - 1 for node in list(curr_component)]):
                    
                    result += 1

        return result
                
