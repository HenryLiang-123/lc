from collections import deque
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj_list = defaultdict(list)
        n = len(edges)

        for i in range(n):
            src, dst = edges[i]
            adj_list[src].append(dst)
            adj_list[dst].append(src)
        result = []
        seen = set()
        def dfs(node, path):
            # path for bob
            if node == 0:
                path.append(0)
                result.append(path[:])
                return True

            seen.add(node)
            for nei in adj_list[node]:
                if nei not in seen:
                    path.append(node)
                    if dfs(nei, path):
                        return True
                    path.pop()

            return False

        dfs(bob, [])
        bob_path = result[0]
        bob_node_to_time = {bob_path[i]:i for i in range(len(bob_path))}
 
        def bfs(node):
            q = deque([(node, 0, 0)])
            seen = set()
            seen.add(node)
            max_amount = float('-inf')
            while q:
                node, time, path_sum = q.popleft()
                if node in bob_node_to_time:
                    if time == bob_node_to_time[node]:
                        path_sum += amount[node] / 2
                    elif time < bob_node_to_time[node]:
                        path_sum += amount[node]
                else:
                    path_sum += amount[node]
                if len(adj_list[node]) == 1 and adj_list[node][0] in seen:
                    max_amount = max(max_amount, path_sum)
                for nei in adj_list[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append((nei, time + 1, path_sum))

            return max_amount

        return int(bfs(0))


                
                









            