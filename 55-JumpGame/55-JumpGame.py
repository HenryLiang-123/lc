// Last updated: 3/14/2025, 4:49:51 PM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        n = len(nums)

        for i in range(n):
            

            if i > furthest:
                return False

            furthest = max(furthest, i + nums[i])

        return True