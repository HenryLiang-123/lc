# Last updated: 3/23/2025, 3:26:18 PM
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # bfs (dijkstra) with tracking of cost to node, if less, reset count to ways to curr_node, and change cost. If equal, ways to nei = ways to nei + ways to curr_node
        MOD = 10**9 + 7
        adj_list = defaultdict(list)
        for src, dst, cost in roads:
            adj_list[src].append((dst, cost))
            adj_list[dst].append((src, cost))

        cost_to_node = {i: float('inf') for i in range(n)}
        cost_to_node[0] = 0
        ways_to_node = {i: 0 for i in range(n)}
        ways_to_node[0] = 1

        def bfs(src):
            q = [(0, 0)]
            heapq.heapify(q)
            while q:
                cost, node = heapq.heappop(q)
                if cost > cost_to_node[node]:
                    continue
                for nei, cost_to_nei in adj_list[node]:    

                    if cost + cost_to_nei < cost_to_node[nei]:
                        cost_to_node[nei] = cost + cost_to_nei
                        heapq.heappush(q, (cost + cost_to_nei, nei))
                        ways_to_node[nei] = ways_to_node[node]
                        
                    elif cost + cost_to_nei == cost_to_node[nei]:
                        ways_to_node[nei] = (ways_to_node[node] + ways_to_node[nei]) % MOD
                       


        bfs(0)
        return ways_to_node[n-1]

            
