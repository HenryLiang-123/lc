# Last updated: 3/23/2025, 3:54:32 PM
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for i in range(len(flights)):
            start, end, price = flights[i]  
            adj_list[start].append((end, price))

        cost_to_node = {(i,0):float("inf") for i in range(n)}
        cost_to_node[(src, 0)] = 0
        
        def bfs():
            q = [(0, src, 0)] # cost, node, level
            heapq.heapify(q)
            while q:
                cost, node, level = heapq.heappop(q)
                if node == dst:
                    return cost
                if cost > cost_to_node[(node, level)]:
                    continue
                if level > k:
                    continue

                for nei, price in adj_list[node]:
                    if cost + price < cost_to_node.get((nei, level+1), float('inf')):
                        cost_to_node[(nei, level+1)] = cost + price
                        heapq.heappush(q, (cost + price, nei, level + 1))


            return -1
        return bfs()
        # result = cost_to_node[dst]

        # if result == float("inf"):
        #     return -1
        # return result
                    






