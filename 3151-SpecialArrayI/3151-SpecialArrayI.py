class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        for i in range(1, n):
            prev = nums[i-1]
            curr = nums[i]
            if prev & 1 == curr & 1:
                return False
        return True