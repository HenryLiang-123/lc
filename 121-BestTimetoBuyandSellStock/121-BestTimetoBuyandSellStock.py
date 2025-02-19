class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_so_far = float('inf')
        profit = float('-inf')
        for i in range(n):
            min_so_far = min(min_so_far, prices[i])
            profit = max(profit, prices[i] - min_so_far)

        return profit