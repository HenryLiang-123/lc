class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        result = 0
        xor = nums[0]

        if n == 1:
            return 1

        for right in range(1, n):
            while xor & nums[right] != 0 and left < right:
                xor ^= nums[left]
                left += 1

            window = right - left + 1
            xor = xor ^ nums[right]

            result = max(result, window)

        return result

            


