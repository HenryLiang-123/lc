class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        new = []
        n = len(prices)
        for i in range(n):
            idx = None
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    idx = j
                    break
            if idx:
                discount = prices[idx]
            else:
                discount = 0

            new.append(prices[i] - discount)

        return new            