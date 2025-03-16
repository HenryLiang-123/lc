// Last updated: 3/15/2025, 9:02:21 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = float('-inf')
        sold = float('-inf')
        cooled = 0
        n = len(prices)

        for i in range(n):
            temp_bought = bought
            temp_sold = sold
            
            bought = max(bought, cooled - prices[i])
            sold = max(sold, temp_bought + prices[i])
            cooled = max(cooled, temp_sold)
            

        return max(bought, sold, cooled, 0)