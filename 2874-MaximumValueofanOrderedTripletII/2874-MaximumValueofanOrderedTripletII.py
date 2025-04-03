# Last updated: 4/3/2025, 4:46:42 PM
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # keep track of max_so_far, get max_diff by subtracting the current number
        # next iteration, we check the result since i < j < k
        result, max_so_far, max_diff = 0,0,0
        n = len(nums)
        for i in range(n):
            result = max(result, max_diff * nums[i])
            max_so_far = max(max_so_far, nums[i])
            max_diff = max(max_diff, max_so_far - nums[i])
        
        return result
