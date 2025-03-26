# Last updated: 3/26/2025, 4:09:21 PM
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        n = len(grid)
        m = len(grid[0])
        
        nums = []

        for i in range(n):
            for j in range(m):
                nums.append(grid[i][j])
        
        nums.sort()
        n = len(nums)

        if len(nums) % 2 != 0:
            median = nums[int(((n+1)/2) - 1)]
        else:
            median = nums[int(n/2 - 1)]

        result = 0
        for element in nums:
            if (element - median) % x != 0:
                return -1
            else:
                result += abs(element - median) / x

        return int(result)