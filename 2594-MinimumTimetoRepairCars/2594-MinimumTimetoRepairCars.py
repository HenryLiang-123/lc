import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        n = len(ranks)
        left = 0
        # max time
        right = max(ranks) * pow(math.ceil(cars / n), 2)

        print(right)

        def can_repair(time):
            repaired = 0
            for i in range(n):
                repaired += math.floor(math.sqrt(time / ranks[i]))

            return repaired >= cars

        while left <= right:
            mid = (left + right) // 2
            if can_repair(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left




