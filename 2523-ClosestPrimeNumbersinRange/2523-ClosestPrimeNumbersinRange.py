// Last updated: 3/12/2025, 5:24:44 PM
import math
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True for _ in range(right+1)]
        sieve[0] = sieve[1] = False

        end = math.ceil(math.sqrt(right))
        for i in range(end+1):
            if sieve[i]:
                for j in range(i*i, right+1, i):
                    sieve[j] = False
        result = []
        for num, is_prime in enumerate(sieve):
            if is_prime and num >= left:
                result.append(num)

        if len(result) < 2:
            return [-1, -1]
        diff = float('inf')
        final = []
        for i in range(1, len(result)):
            if result[i] - result[i-1] < diff:
                final = [result[i-1], result[i]]
                diff = result[i] - result[i-1]

        return final
