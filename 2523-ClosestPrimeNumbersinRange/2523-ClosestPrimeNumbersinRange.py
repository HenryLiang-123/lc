import math
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True for _ in range(right+1)]
        prime[0], prime[1] = False, False

        divisors = math.floor(math.sqrt(right))

        for i in range(2, divisors + 1):
            if prime[i]:
                for j in range(i*i, right+1, i):
                    prime[j] = False
        nums = []
        for num in range(left, right+1):
            if prime[num]:
                nums.append(num)
        result = float('inf')
        ret = [-1,-1]
        for i in range(1, len(nums)):
            dist = nums[i] - nums[i-1]
            if dist < result:
                result = min(result, dist)
                ret[0] = nums[i-1]
                ret[1] = nums[i]

        return ret


