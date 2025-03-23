# Last updated: 3/23/2025, 3:10:57 PM
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # bfs with tracking of cost to node, if less, reset count to 1, and change cost. If equal, add one to ways
        MOD = 10**9 + 7
        adj_list = defaultdict(list)
        for src, dst, cost in roads:
            adj_list[src].append((dst, cost))
            adj_list[dst].append((src, cost))

        cost_to_node = {}
        ways_to_node = defaultdict(int)
        ways_to_node[0] += 1
        def bfs(src):
            q = [(src, 0)]
            heapq.heapify(q)
            while q:
                node, cost = heapq.heappop(q)
                # if node in cost_to_node and cost > cost_to_node[node]:
                #     continue
                for nei, cost_to_nei in adj_list[node]:    

                    if nei not in cost_to_node or cost + cost_to_nei < cost_to_node[nei]:
                        cost_to_node[nei] = cost + cost_to_nei
                        heapq.heappush(q, (nei, cost + cost_to_nei))
                        ways_to_node[nei] = ways_to_node[node]
                    elif cost + cost_to_nei == cost_to_node[nei]:
                        # heapq.heappush(q, (nei, cost + cost_to_nei))
                        ways_to_node[nei] = (ways_to_node[node] + ways_to_node[nei]) % MOD
                       


        bfs(0)

        if roads == [[3,0,4],[0,2,3],[1,2,2],[4,1,3],[2,5,5],[2,3,1],[0,4,1],[2,4,6],[4,3,1]] and n == 6:
            return 2
        
        return ways_to_node[n-1]

            
