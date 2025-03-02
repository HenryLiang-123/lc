class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0 for _ in range(n+1)]
        buy, sell = float('-inf'), 0

        for i in range(1, n+1):
            buy = max(buy, sell - prices[i-1]) # keep, buy
            sell = max(sell, buy + prices[i-1])
            dp[i] = max(buy, sell)

        return dp[-1]
            

