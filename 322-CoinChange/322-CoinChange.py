// Last updated: 3/6/2025, 9:41:31 PM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = float('inf')
        memo = {}
        def dfs(path_sum):
            if path_sum in memo:
                return memo[path_sum]
            if path_sum == amount:
                return 0

            if path_sum > amount:
                return float('inf')

            min_coins = float('inf')
            for c in coins:
                path_sum += c
                res = dfs(path_sum)
                if res != float('inf'):
                    min_coins = min(res+1, min_coins)
                # res += dfs(path_sum)
                path_sum -= c

            memo[(path_sum)] = min_coins

            
            return min_coins

        result = dfs(0)
        return result if result != float('inf') else -1
                





