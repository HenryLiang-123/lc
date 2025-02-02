class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        search_needed = False
        if n <= 1:
            return True
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                search_needed = True
                break
        if search_needed:
            if nums[i] > nums[0]:
                return False
            for j in range(i+1, n):
                if nums[j] < nums[j-1] or nums[j] > nums[0]:
                    return False

        return True