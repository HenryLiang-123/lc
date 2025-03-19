// Last updated: 3/19/2025, 2:18:58 PM
class Solution:
    def jump(self, nums: List[int]) -> int:
        levels = 0
        n = len(nums)
        level_start = 0
        level_end = 0
        furthest = 0

        while level_end < n-1:
            for i in range(level_start, level_end+1):
                furthest = max(furthest, i + nums[i])
            level_start = level_end + 1
            level_end = furthest
            levels += 1


                


        return levels
