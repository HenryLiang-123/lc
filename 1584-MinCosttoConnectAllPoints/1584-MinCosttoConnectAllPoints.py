import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj_list = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj_list[i].append((cost, j))
                adj_list[j].append((cost, i))
                
        seen = set()
        minHeap = [(0, 0)] # cost, node
        heapq.heapify(minHeap)

        def bfs():
            res = 0
            while minHeap:
                curr_cost, curr_node = heapq.heappop(minHeap)
                if curr_node in seen:
                    continue
                seen.add(curr_node)
                res += curr_cost
                for cost_to_nei, nei in adj_list[curr_node]:
                    if nei not in seen:
                        heapq.heappush(minHeap, (cost_to_nei, nei))


            return res

        result = bfs()
        return result
        # print(cost_to_node)
