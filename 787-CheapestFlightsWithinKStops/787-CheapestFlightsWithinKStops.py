# Last updated: 3/23/2025, 3:33:07 PM
from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = {}
        for i in range(len(flights)):
            start, end, price = flights[i]
            if start not in adj_list:
                adj_list[start] = [(end, price)]
            else:
                adj_list[start].append((end, price))

        cost_to_node = [float("inf") for _ in range(n)]
        
        def bfs():
            q = deque([(src, 0, 0)])
            min_cost = float("inf")
            while q:
                node, cost, level = q.popleft()
                if node == dst:
                    min_cost = min(min_cost, cost_to_node[node])
                    # return cost_to_node[node]
                if level < k + 1:
                    if node in adj_list:
                        for nei, price in adj_list[node]:
                            if cost + price < cost_to_node[nei]:
                                cost_to_node[nei] = cost + price
                                q.append((nei, cost + price, level + 1))

            return min_cost

        result = bfs()
        if result == float("inf"):
            return -1
        return result
                    






