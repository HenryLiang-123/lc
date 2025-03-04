from collections import Counter
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)
        counts = Counter(data)
        ones = counts[1]
        left = 0
        count_map = {
            1:0,
            0:0
        }
        least_zeros = float('inf')
        for right in range(n):
            print(count_map)
            count_map[data[right]] += 1
            window_size = right - left + 1
            if window_size > ones:
                count_map[data[left]] -= 1
                window_size -= 1
                left += 1
            # print(least_zeros)
            if window_size == ones:
                least_zeros = min(least_zeros, count_map[0])

        return least_zeros
            
