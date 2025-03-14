// Last updated: 3/14/2025, 4:09:01 PM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]

        if n == 1:
            return max_so_far
    
        for i in range(1, n):

            result = max(nums[i], result, max_so_far * nums[i], min_so_far * nums[i])
            temp = max_so_far
            max_so_far = max(nums[i], max_so_far * nums[i], min_so_far * nums[i])
            min_so_far = min(nums[i], temp * nums[i], min_so_far * nums[i])
            
            


        return result