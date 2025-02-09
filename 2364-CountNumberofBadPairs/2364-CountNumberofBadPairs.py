import math
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        diff = {}
        n = len(nums)
        for i in range(n):
            diff[nums[i]-i] = diff.get(nums[i]-i, 0) + 1

        good = 0
        for key, value in diff.items():
            if value >= 2:
                good += math.comb(value, 2)
        
        total = math.comb(n, 2)

        return total - good


        