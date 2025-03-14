// Last updated: 3/14/2025, 5:44:03 PM
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        res = 0

        while right < n-1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            left = right + 1
            right = farthest
            res += 1

        return res




            
