class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        n = len(nums)
        window_size = 0
        result = float('-inf')
        for right in range(n):
            if nums[right] == 1:
                window_size = right - left + 1
            else:
                zero_count += 1
                while zero_count > 1:
                    if nums[left] == 0:
                        zero_count -= 1
                    left += 1
                window_size = right - left + 1

            result = max(result, window_size)
                    



        return result

