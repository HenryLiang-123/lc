# Last updated: 4/5/2025, 4:57:25 PM
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        def dfs(start, path_sum):
            nonlocal result
            result += path_sum

            for i in range(start, n):
                path_sum ^= nums[i]
                dfs(i+1, path_sum)
                path_sum ^= nums[i]

        dfs(0, 0)
        return result