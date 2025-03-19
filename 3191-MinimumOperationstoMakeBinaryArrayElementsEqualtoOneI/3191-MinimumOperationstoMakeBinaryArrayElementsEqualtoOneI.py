// Last updated: 3/19/2025, 1:55:30 PM
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        operations = 0
        for right in range(n):
            window = right - left + 1
            if window < 3:
                continue
            elif window == 3:
                if nums[left] == 0:
                    operations += 1
                    for i in range(left, right+1):
                        if nums[i] == 1:
                            nums[i] = 0
                        else:
                            nums[i] = 1
                left += 1

            
        return operations if sum(nums) ==  n else -1             


                        