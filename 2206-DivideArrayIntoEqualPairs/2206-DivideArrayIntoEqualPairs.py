from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)
        counts = Counter(nums)

        for key, value in counts.items():
            if value % 2 != 0:
                return False

        return True
