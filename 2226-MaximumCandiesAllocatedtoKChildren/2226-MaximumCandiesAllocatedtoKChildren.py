class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        def can_allocate(c):
            # can allocate c candies to k children
            allocation = 0
            for i in range(n):
                curr_alloc = candies[i] // c
                allocation += curr_alloc

            return allocation >= k

        left = 1
        right = max(candies)

        while left <= right:
            mid = (left + right) // 2
            if can_allocate(mid):
                left = mid + 1
            else:
                right = mid - 1

        return left-1
