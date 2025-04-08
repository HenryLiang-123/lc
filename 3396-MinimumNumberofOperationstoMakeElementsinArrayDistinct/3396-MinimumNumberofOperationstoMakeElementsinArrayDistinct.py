# Last updated: 4/8/2025, 4:34:10 PM
from collections import Counter
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        result = 0 
        n = len(nums)

        def is_valid(d):
            for key, value in d.items():
                if value > 1:
                    return False

            return True

        if len(nums) <= 3:
            if is_valid(counts):
                return 0
            return 1

        for i in range(2, n, 3):
            e1, e2, e3 = nums[i], nums[i-1], nums[i-2]
            if is_valid(counts):
                return result
            else:
                counts[e1] -= 1
                counts[e2] -= 1
                counts[e3] -= 1
                result += 1

        if i < n-1:
            if not is_valid(counts):
                result +=1

        return result
        
