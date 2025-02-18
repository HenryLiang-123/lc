// Last updated: 2/18/2025, 1:50:07 PM
class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        def dfs(left, right):
            if right <= left:
                return 1

            if (left, right) in memo:
                return memo[(left, right)]

            total = 0
            for root in range(left, right + 1):
                left_trees = dfs(left, root - 1)
                right_trees = dfs(root+1, right)
                total += left_trees * right_trees

            memo[(left, right)] = total
            return memo[(left, right)]

        return dfs(1, n)