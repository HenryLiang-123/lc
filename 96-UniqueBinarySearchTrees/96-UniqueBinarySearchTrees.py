// Last updated: 2/28/2025, 7:31:56 PM
class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        def dfs(left, right):
            if (left, right) in memo:
                return memo[(left, right)]

            if left >= right:
                return 1

            res = 0
            for i in range(left, right+1):
                left_trees = dfs(left, i-1)
                right_trees = dfs(i+1, right)
                res += left_trees * right_trees
                
            memo[(left, right)] = res
            return memo[(left, right)]

        return (dfs(0, n-1))

            