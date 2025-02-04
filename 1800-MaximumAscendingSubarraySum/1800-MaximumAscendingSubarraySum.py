class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        result = curr_sum = nums[0]
        for right in range(1, n):
            
            curr_sum += nums[right]
            if nums[right] <= nums[right-1]:
                while left < right:
                    curr_sum -= nums[left]
                    left += 1

            result = max(result, curr_sum)

        return result