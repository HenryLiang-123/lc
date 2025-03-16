// Last updated: 3/15/2025, 10:17:06 PM
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        result = prices.copy()
        for i in range(n):
            
            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                result[idx] -= prices[i]

            stack.append(i)
        # intermediate = stack + insertions

        # for element, loc in intermediate:
        #     result[loc] = element

        return result
