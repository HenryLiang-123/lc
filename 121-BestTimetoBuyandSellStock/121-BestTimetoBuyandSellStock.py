// Last updated: 3/2/2025, 4:24:55 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        result = 0
        min_so_far = float('inf')
        for i in range(n):
            min_so_far = min(min_so_far, prices[i])
            result = max(result, prices[i] - min_so_far)

        return result