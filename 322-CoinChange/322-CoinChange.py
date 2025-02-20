// Last updated: 2/20/2025, 2:48:43 PM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(path_sum):
            if path_sum in memo:
                return memo[path_sum]
            if path_sum == amount:
                memo[path_sum] = 0
                return 0

            if path_sum > amount:
                memo[path_sum] = float('inf')
                return float('inf')

            min_coins = float("inf")
            for c in coins:
                min_coins = min(min_coins, dfs(path_sum + c))
                
            memo[path_sum] = min_coins + 1
            return memo[path_sum]

        result = dfs(0)
        return result if result != float('inf') else -1

        