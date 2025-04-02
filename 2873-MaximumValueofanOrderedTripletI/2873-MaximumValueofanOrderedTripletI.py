# Last updated: 4/2/2025, 3:58:18 PM
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        result = float('-inf')
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    result = max(result, (nums[i]-nums[j]) * nums[k])

        return max(result, 0)
