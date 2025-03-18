// Last updated: 3/18/2025, 2:26:20 PM
class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        def dfs(left, right):
            
            if (left, right) in memo:
                return memo[(left, right)]

            if left > right:
                return 1
            
            result = 0

            for i in range(left, right+1):
                result += dfs(left, i-1) * dfs(i+1, right)

            memo[(left, right)] = result

            return memo[(left, right)]

        return dfs(0, n-1)