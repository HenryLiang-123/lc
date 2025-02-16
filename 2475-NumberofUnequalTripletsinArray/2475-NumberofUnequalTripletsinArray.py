class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        n = len(nums)
        target = sum(nums) / 2
        memo = {}
        def dfs(start, used, path_sum):

            if (used, path_sum) in memo:
                return memo[(used, path_sum)]

            if used < n and path_sum == target:
                return True

            if used < n and path_sum > target:
                return False

            for i in range(start, n):
                path_sum += nums[i]
                if dfs(i+1, used+1, path_sum):
                    memo[(used+1, path_sum)] = True
                    return True
                path_sum -= nums[i]
            memo[(used, path_sum)] = False
            return False

        return (dfs(0, 0, 0))

            
