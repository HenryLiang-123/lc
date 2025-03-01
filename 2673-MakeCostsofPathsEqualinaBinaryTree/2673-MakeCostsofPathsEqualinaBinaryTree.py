// Last updated: 2/28/2025, 7:09:14 PM
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        result = 0
        def dfs(node):
            nonlocal result

            if node >= n:
                return 0

            left_val = dfs(2*(node+1)-1)
            right_val = dfs(2*(node+1))

            result += abs(left_val - right_val)

            return max(left_val, right_val) + cost[node]

        dfs(0)
        return result