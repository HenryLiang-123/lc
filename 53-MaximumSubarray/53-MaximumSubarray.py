class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_sum = 0
        result = float('-inf')
        n = len(nums)

        for i in range(n):
            curr_sum += nums[i]
            if curr_sum < 0:
                curr_sum = 0

            result = max(result, curr_sum)
        
        if max(nums) < 0:
            return max(nums)

        return result