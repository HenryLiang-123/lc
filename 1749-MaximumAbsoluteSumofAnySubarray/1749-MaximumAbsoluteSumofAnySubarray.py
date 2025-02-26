class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_sum_p = 0
        curr_sum_n = 0
        n = len(nums)
        max_sum = float('-inf')
        min_sum = float('inf')
        for i in range(n):
            curr_sum_p += nums[i]
            curr_sum_n += nums[i]

            if curr_sum_p < 0:
                curr_sum_p = 0
            
            if curr_sum_n > 0:
                curr_sum_n = 0

            max_sum = max(curr_sum_p, max_sum)
            min_sum = min(curr_sum_n, min_sum)

        return max(abs(min_sum), abs(max_sum))
