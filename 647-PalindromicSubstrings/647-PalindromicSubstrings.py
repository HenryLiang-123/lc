class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def expand(left, right):
            substrs = 0
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                    substrs += 1
                else:
                    break

            return substrs
        result = 0
        for i in range(n):
            even_center = expand(i, i+1)
            odd_center = expand(i, i)
            result += even_center + odd_center

        return result



