// Last updated: 3/16/2025, 1:44:24 PM
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        h = [(-counts[i], i) for i in counts.keys()]
        heapq.heapify(h)
        result = []
        while True:
            freq, element = heapq.heappop(h)
            result.append(element)
            k -= 1
            if k == 0:
                return result
             