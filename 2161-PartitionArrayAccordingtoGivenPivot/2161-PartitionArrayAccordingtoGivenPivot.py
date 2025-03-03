// Last updated: 3/3/2025, 1:15:48 PM
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        i, j = 0, n-1
        i2, j2 = 0, n-1
        res = [0 for _ in range(n)]
        while i < n:
            if nums[i] < pivot:
                res[i2] = nums[i]
                i2 += 1
            if nums[j] > pivot:
                res[j2] = nums[j]
                j2 -= 1

            i += 1
            j -= 1

        while i2 <= j2:
            res[i2] = pivot
            res[j2] = pivot
            i2 += 1
            j2 -= 1

        return res

                

        # less = []
        # more = []
        # pivots = []
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] < pivot:
        #         less.append(nums[i])
        #     elif nums[i] == pivot:
        #         pivots.append(nums[i])
        #     elif nums[i] > pivot:
        #         more.append(nums[i])

        # return less + pivots + more