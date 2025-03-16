class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = -prices[0]
        sold = float('-inf')
        cooled = 0
        n = len(prices)

        for i in range(1, n):
            temp_bought = bought
            temp_sold = sold
            
            bought = max(bought, cooled - prices[i])
            sold = max(sold, temp_bought + prices[i])
            cooled = max(cooled, temp_sold)
            
            print(bought, sold, cooled)

        return max(bought, sold, cooled, 0)