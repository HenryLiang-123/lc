# Last updated: 3/25/2025, 3:39:32 PM
import heapq
class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        # dijkstra
        adj_list = defaultdict(list)
        for src, dst, cost in edges:
            adj_list[src].append((dst, cost))

        cost_to_node = {i:float('inf') for i in range(n)}
        def bfs(src):
            q = [(0, src)]
            cost_to_node[src] = 0
            heapq.heapify(q)
            while q:
                cost, node = heapq.heappop(q)
                for nei, cost_to_nei in adj_list[node]:
                    new_cost = cost + cost_to_nei
                    if new_cost < cost_to_node[nei]:
                        cost_to_node[nei] = new_cost
                        heapq.heappush(q, (new_cost, nei))

        bfs(s)
        result = float('inf')
        for dst in marked:
            result = min(result, cost_to_node[dst])

        if result == float('inf'):
            return -1

        return result