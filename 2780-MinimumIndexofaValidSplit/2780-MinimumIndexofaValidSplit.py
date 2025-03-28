# Last updated: 3/28/2025, 1:55:48 PM
from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counts = Counter(nums)
        mode = max(counts, key = counts.get)
        mode_counts = counts[mode]

        n = len(nums)
        curr_count = 0

        for i in range(n):
            window = i+1
            if nums[i] == mode:
                curr_count += 1
            
            # test validity
            if curr_count * 2 > window and (mode_counts - curr_count) * 2 > (n-i-1):
                return i

        return -1