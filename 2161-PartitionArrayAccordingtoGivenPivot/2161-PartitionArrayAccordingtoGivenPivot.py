class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        more = []
        pivots = []
        n = len(nums)
        for i in range(n):
            if nums[i] < pivot:
                less.append(nums[i])
            elif nums[i] == pivot:
                pivots.append(nums[i])
            elif nums[i] > pivot:
                more.append(nums[i])

        return less + pivots + more