// Last updated: 3/11/2025, 3:06:10 PM
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # find invalid
        left = 0
        n = len(s)
        d = {"a":0, "b":0, "c":0}
        def is_valid(freq_dict): 
            for key, value in freq_dict.items():
                if value < 1:
                    return False
            return True
            
        result = 0
        for right in range(n):
            d[s[right]] += 1
            while is_valid(d):
                result += n - right
                d[s[left]] -= 1
                left += 1


        return result