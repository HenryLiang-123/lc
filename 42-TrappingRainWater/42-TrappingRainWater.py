// Last updated: 2/18/2025, 11:59:28 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]
        right_max = [0]
        n = len(height)
        for i in range(1, n):
            left_max.append(max(left_max[-1], height[i-1]))

        for i in reversed(range(n-1)):
            right_max.append(max(right_max[-1], height[i+1]))

        right_max = right_max[::-1]

        result = 0


        for i in range(n):
            curr = max(min(left_max[i], right_max[i]) - height[i], 0)
            result += curr

        return result