class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
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
                result = dfs(path_sum)
                path_sum -= c
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)

            memo[path_sum] = min_coins
            return memo[path_sum]

        result = dfs(0)
        
        if result != float('inf'):
            return result
        else:
            return -1