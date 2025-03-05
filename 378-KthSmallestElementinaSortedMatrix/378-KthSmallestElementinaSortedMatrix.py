import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        starts = []

        for i, arr in enumerate(matrix):
            starts.append((arr[0], i, 0)) # value, row, col

        heapq.heapify(starts)

        while k > 0:
            value, row, col = heapq.heappop(starts)

            if col < n-1:
                next_element = matrix[row][col+1]
                heapq.heappush(starts, (next_element, row, col+1))

            k -= 1

        return value 