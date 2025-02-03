class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        # increasing
        result_inc = 1
        result_dec = 1
        for right in range(1, n):
            window_size = right - left + 1
            if nums[right] <= nums[right-1]:
                while left < right:
                    window_size -= 1
                    left += 1
            result_inc = max(result_inc, window_size)




        left = 0
        for right in range(1, n):
            window_size = right - left + 1
            if nums[right] >= nums[right-1]:
                while left < right:
                    window_size -= 1
                    left += 1
            result_dec = max(result_dec, window_size)          
        print(result_inc)
        return max(result_inc, result_dec)  


