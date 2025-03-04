// Last updated: 3/4/2025, 12:22:20 PM
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        result = 0
        for i in range(2, n):
            start, end = 0, i-1
            target = arr[i]
            while start < end:
                if arr[start] + arr[end] == target:
                    dp[end][i] = dp[start][end] + 1
                    result = max(result, dp[end][i])
                    start += 1
                    end -= 1
                elif arr[start] + arr[end] < target:
                    start += 1
                elif arr[start] + arr[end] > target:
                    end -= 1

        return result + 2 if result else 0