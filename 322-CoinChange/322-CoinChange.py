// Last updated: 2/18/2025, 4:54:48 PM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dfs(path_sum):
            if path_sum in memo:
                return memo[(path_sum)]

            if path_sum == amount:
                return 0

            if path_sum > amount:
                return float('inf')
            result = float('inf')
            for coin in coins:
                path_sum += coin
                res = dfs(path_sum)
                if res != float('inf'):
                    result = min(result, res+1)
                path_sum -= coin

            memo[path_sum] = result

            return result

        r = dfs(0)
        if r != float('inf'):
            return r
        else:
            return -1

