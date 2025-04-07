# Last updated: 4/7/2025, 12:35:32 PM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        n = len(nums)
        memo = {}
        def dfs(start, path_sum, path):
            if (path_sum, len(path)) in memo:
                return memo[(path_sum, len(path))]

            if len(path) >= n or path_sum > target:
                memo[(path_sum, len(path))] = False
                return False

            if path_sum == target:
                memo[(path_sum, len(path))] = True
                return True

            for i in range(start, n):
                curr = nums[i]
                path.append(curr)
                path_sum += curr
                if dfs(i+1, path_sum, path):
                    memo[(path_sum, len(path))] = True
                    return True

                path.pop()
                path_sum -= curr
            
            memo[(path_sum, len(path))] = False
            return False
        
        return dfs(0, 0, [])