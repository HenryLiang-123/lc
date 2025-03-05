class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = n-1, n-1

        while i >= 0:
            if i == n-1:
                i -= 1
                continue
            if nums[i] < nums[i+1]:
                break
            else:
                i -= 1
        if i != -1:
            while j >= 0:
                if nums[j] > nums[i]:
                    break
                else:
                    j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]
            sorted_part = nums[i+1:][::-1]
            nums[i+1:] = sorted_part
        else:
            nums[0:] = nums[::-1]