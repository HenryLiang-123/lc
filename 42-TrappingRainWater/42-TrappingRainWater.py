class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0 for _ in range(n)]
        max_right = [0 for _ in range(n)]
        rain = [0 for _ in range(n)]

        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i-1])

        for i in reversed(range(n-1)):
            max_right[i] = max(max_right[i+1], height[i+1])

        for i in range(n):
            rain[i] = max(min(max_right[i], max_left[i]) - height[i], 0)

        return sum(rain)