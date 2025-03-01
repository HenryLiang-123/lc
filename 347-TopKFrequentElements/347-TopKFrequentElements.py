from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        arr = [(-counts[i], i) for i in counts.keys()]
        
        heapq.heapify(arr)

        result = []
        for i in range(k):
            curr = heapq.heappop(arr)
            result.append(curr[1])

        return result
