// Last updated: 3/15/2025, 9:14:46 PM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        n = len(nums)
        result = nums[0]

        for i in range(1, n):
            result = max(result, nums[i], max_so_far * nums[i], min_so_far * nums[i])

            temp_max_so_far = max_so_far
            max_so_far = max(nums[i], max_so_far*nums[i], min_so_far * nums[i])
            min_so_far = min(nums[i], temp_max_so_far*nums[i], min_so_far * nums[i])

        return result

