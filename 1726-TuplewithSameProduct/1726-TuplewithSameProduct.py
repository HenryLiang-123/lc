import math
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                product_count[product] = product_count.get(product, 0) + 1

        result = 0
        for key, value in product_count.items():
            if value >= 2:
                result += math.perm(value, 2) * 4

        return result
