from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        adj_list = defaultdict(list)
        # source -> destintion, value
        for i in range(n):
            src, dst = equations[i]
            value = values[i]
            adj_list[src].append((dst, value))
            adj_list[dst].append((src, 1 / value))

        def bfs(src, dst):
            q = deque([(src, 1)]) #node, curr_val
            seen = set([src])

            while q:
                node, value = q.popleft()
                if node == dst:
                    return value

                for nei, multiplier in adj_list[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append((nei, value * multiplier))
            return -1.0
        result = []
        for n1, n2 in queries:
            if n1 not in adj_list or n2 not in adj_list:
                result.append(-1.0)
            else:
                v = bfs(n1, n2)
                result.append(v)

        return result
