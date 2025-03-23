# Last updated: 3/23/2025, 3:20:09 PM
import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        adj_list = defaultdict(list)
        for src, dst, cost in roads:
            adj_list[src].append((dst, cost))
            adj_list[dst].append((src, cost))

        # Initialize distances to infinity except for source node
        cost_to_node = {i: float('inf') for i in range(n)}
        cost_to_node[0] = 0
        
        ways_to_node = [0] * n
        ways_to_node[0] = 1
        
        # Priority queue storing (cost, node)
        pq = [(0, 0)]  # (cost, node)
        
        while pq:
            curr_cost, node = heapq.heappop(pq)
            
            # Skip if we've found a better path already
            if curr_cost > cost_to_node[node]:
                continue
                
            for nei, edge_cost in adj_list[node]:
                new_cost = curr_cost + edge_cost
                
                # Found a shorter path
                if new_cost < cost_to_node[nei]:
                    cost_to_node[nei] = new_cost
                    ways_to_node[nei] = ways_to_node[node]
                    heapq.heappush(pq, (new_cost, nei))
                # Found another path with the same cost
                elif new_cost == cost_to_node[nei]:
                    ways_to_node[nei] = (ways_to_node[nei] + ways_to_node[node]) % MOD
        
        return ways_to_node[n-1]