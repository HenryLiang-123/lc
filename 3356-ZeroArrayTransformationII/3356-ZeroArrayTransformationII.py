// Last updated: 3/13/2025, 2:31:25 PM
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def can_achieve(k):
            n = len(nums)
            diff_arr = [0 for _ in range(n)]

            for i in range(k):
                start, end, value = queries[i]
                diff_arr[start] -= value
                if end < n-1:
                    diff_arr[end+1] += value

            # for i in range(1, n):
            #     diff_arr[i] = diff_arr[i-1] + diff_arr[i]
            curr = 0
            for i in range(n):
                curr += diff_arr[i]
                if curr + nums[i] > 0:
                    return False

            return True

        left = 0
        right = len(queries)

        while left <= right:
            mid = (left + right) // 2
            if can_achieve(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left if left <= len(queries) else -1
