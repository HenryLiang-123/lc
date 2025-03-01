class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        def swap_0(l):
            left = 0
            n = len(l)
            for right in range(n):
                if l[right] != 0:
                    l[left], l[right] = l[right], l[left]
                    left += 1

            return nums

        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        return swap_0(nums)
