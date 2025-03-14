class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        def solve(subset):
            n = len(subset)
            if n == 1:
                return subset[0]
            dp = [0 for _ in range(n)]
            dp[0] = subset[0]
            dp[1] = max(subset[0], subset[1])

            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + subset[i])

            return dp[-1]

        return max(solve(nums[:(len(nums)-1)]), solve(nums[1:]))