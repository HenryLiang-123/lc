# Last updated: 4/7/2025, 12:43:31 PM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        # nums.sort()
        if sum(nums) % 2 != 0:
            return False

        n = len(nums)

        target = sum(nums) // 2
        def dfs(start, path_sum, path_len):
            if (path_len, path_sum) in memo:
                return memo[(path_len, path_sum)]

            if path_sum > target:
                memo[(path_len, path_sum)] = False
                return False

            if path_sum == target:
                memo[(path_len, path_sum)] = True
                return True

            for i in range(start, n):
                path_sum += nums[i]
                path_len += 1
                if dfs(i+1, path_sum, path_len):
                    memo[(path_len, path_sum)] = True
                    return True
                path_sum -= nums[i]
                path_len -= 1

            memo[(path_len, path_sum)] = False
            return False

        return dfs(0, 0, 0)
