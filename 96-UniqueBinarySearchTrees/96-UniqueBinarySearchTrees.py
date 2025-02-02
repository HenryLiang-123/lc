class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        def dfs(left, right):
            if right <= left:
                return 1

            if (left, right) in memo:
                return memo[(left, right)]
            
            total = 0

            for root in range(left, right+1):
                left_bst = dfs(left, root-1)
                right_bst = dfs(root+1, right)
                total += left_bst * right_bst

            memo[(left, right)] = total
            return memo[(left, right)]

        return dfs(0, n-1)
            
