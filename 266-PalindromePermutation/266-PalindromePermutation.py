from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        #one odd
        counts = Counter(s)
        odd_count = 0
        for key, value in counts.items():
            if value % 2 != 0:
                odd_count += 1

        return odd_count <= 1
