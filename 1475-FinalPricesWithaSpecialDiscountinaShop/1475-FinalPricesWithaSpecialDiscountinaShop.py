// Last updated: 3/15/2025, 10:07:16 PM
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [(prices[0], 0)]
        n = len(prices)
        result = [0 for _ in range(n)]
        insertions = []
        for i in range(1, n):
            
            while stack and prices[i] <= stack[-1][0]:
                top, idx = stack.pop()
                final = top - prices[i]
                insertions.append((final, idx))

            stack.append((prices[i], i))
            # result += curr_result[::-1]
        intermediate = stack + insertions

        for element, loc in intermediate:
            result[loc] = element

        return result

        # for element, loc in stack:
        #     result.insert(loc, element)

        # return result
