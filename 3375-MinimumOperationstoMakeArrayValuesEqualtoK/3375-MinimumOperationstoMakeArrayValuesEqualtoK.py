# Last updated: 4/9/2025, 5:37:53 PM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        count_equal = 0
        n = len(nums)
        result = 0

        for i in range(n):
            if nums[i] < k:
                return -1
            elif nums[i] > k:
                seen.add(nums[i])
            

        return len(seen)

            