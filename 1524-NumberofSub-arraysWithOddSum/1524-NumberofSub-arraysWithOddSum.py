from collections import Counter
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        result = []
        n = len(arr)
        
        odd_prefix = 0
        even_prefix = 1
        curr_sum = 0
        res = 0
        MOD = 10**9 + 7
        for i in range(n):
            curr_sum += arr[i]

            if curr_sum % 2 == 0:
                res += odd_prefix
                even_prefix += 1
            else:
                res += even_prefix
                odd_prefix += 1

        return res % MOD

            
        
