import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums2)
        elements = [(nums2[i], nums1[i]) for i in range(n)]
        elements.sort(reverse=True)
        h = []
        heapq.heapify(h)
        max_sum = 0
        result = float('-inf')
        for i in range(n):
            e2, e1 = elements[i]
            if i < k-1:
                heapq.heappush(h, e1)
                max_sum += e1
            elif i == k-1:
                heapq.heappush(h, e1)
                max_sum += e1
                result = max(result, max_sum * e2)
            else:
                heapq.heappush(h, e1)
                smallest = heapq.heappop(h)
                max_sum += e1
                max_sum -= smallest
                result = max(result, max_sum * e2)

        return result





                
