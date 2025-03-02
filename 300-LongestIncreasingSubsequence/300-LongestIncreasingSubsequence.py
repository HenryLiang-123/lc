class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = 1

        for i in range(1, n):
            to_check = [dp[j] for j in range(i) if nums[j] < nums[i]]
            if to_check:
                dp[i] = 1 + max(to_check)
            else:
                dp[i] = 1
        # print(dp)
        return max(dp)