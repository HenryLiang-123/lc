class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n+1)]
        prev_min = [0 for _ in range(n+1)]
        prev_max = [0 for _ in range(n+1)]
        dp[0] = 1
        prev_max[0] = 1
        prev_min[0] = 1
        for i in range(1, n+1):
            prev_min[i] = min(nums[i-1], prev_min[i-1] * nums[i-1], prev_max[i-1] * nums[i-1])
            prev_max[i] = max(nums[i-1], prev_max[i-1] * nums[i-1], prev_min[i-1] * nums[i-1])
            dp[i] = max(prev_min[i-1] * nums[i-1], prev_max[i-1] * nums[i-1], nums[i-1])

            
        return max(dp[1:])
