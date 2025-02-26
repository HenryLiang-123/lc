from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for src, dst, cost in times:
            adj_list[src].append((dst, cost))

        node_to_cost = {i: float('inf') for i in range(1, n+1)}
        node_to_cost[k] = 0
        def bfs(node):
            seen = set()
            seen.add(node)
            q = deque([(node, 0)])
            while q:
                node, cost = q.popleft()
                seen.add(node)
                for nei, cost_to_nei in adj_list[node]:
                    if cost + cost_to_nei < node_to_cost[nei]:
                        node_to_cost[nei] = cost + cost_to_nei
                        q.append((nei, cost + cost_to_nei))

            return seen

        seen_set = bfs(k)
        if len(seen_set) != n:
            return -1
        return max(node_to_cost.values())




