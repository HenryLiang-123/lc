import heapq
from collections import Counter
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # keep hash of freq, and max heap of elements. 
        # we take the top element and repeat it maximum of k times. 
        # if left over, take one from next element, and push this top back
        # if not, pop.
        n = len(s)
        freq = Counter(s)
        elements = [(-ord(i), i) for i in list(freq.keys())]
        heapq.heapify(elements)

        result = ""

        while elements:
            o, e = heapq.heappop(elements)
            result += e * min(freq[e], repeatLimit)
            if not elements:
                break

            if freq[e] - repeatLimit > 0:
                freq[e] -= repeatLimit
                next_o, next_element = heapq.heappop(elements)

                if freq[next_element] - 1 > 0:
                    freq[next_element] -= 1
                    heapq.heappush(elements, (next_o, next_element))

                result += next_element
                heapq.heappush(elements, (o, e))

        return (result)


                

                
