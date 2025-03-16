class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dfs(idx, path_sum):
            if (idx, path_sum) in memo:
                return memo[(idx, path_sum)]

            if idx == n:
                return 1 if path_sum == target else 0

            # if idx <path_sum > target:
            #     return 0

            add = dfs(idx + 1, path_sum + nums[idx])
            sub = dfs(idx + 1, path_sum - nums[idx])

            memo[(idx, path_sum)] = add + sub 

            return memo[(idx, path_sum)]

        return dfs(0, 0)