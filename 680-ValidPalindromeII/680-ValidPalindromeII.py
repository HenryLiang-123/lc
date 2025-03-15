class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two pointer from both ends
        # if one pair is unequal, try deleting both and continue. If another pair unequal, return False
        left = 0
        right = len(s) - 1

        def is_pali(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if not is_pali(left+1, right) and not is_pali(left, right - 1):
                    return False
                return True
        
        return True



