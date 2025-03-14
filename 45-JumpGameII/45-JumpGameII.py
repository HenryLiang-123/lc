class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        furthest = 0
        end_of_level = 0
        level = 0
        for i in range(n-1):
            furthest = max(furthest, i + nums[i])

            if i == end_of_level:
                level += 1
                end_of_level = furthest

        return level






            
