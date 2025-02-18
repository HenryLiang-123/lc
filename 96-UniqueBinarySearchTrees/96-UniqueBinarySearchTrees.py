// Last updated: 2/18/2025, 4:30:38 PM
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
                left_tree = dfs(left, i-1)
                right_tree = dfs(i+1, right)
                res += left_tree * right_tree

            memo[(left, right)] = res

            return memo[(left, right)]

        return dfs(1, n)