class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        result = 0
        n = len(arr)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(2, n):
            target = arr[i]
            left, right = 0, i-1
            while left < right:
                if arr[left] + arr[right] == target:
                    dp[right][i] = dp[left][right] + 1
                    result = max(result, dp[right][i])
                    right -= 1
                    left += 1
                elif arr[left] + arr[right] > target:
                    right -= 1
                elif arr[left] + arr[right] < target:
                    left += 1

        return result + 2 if result else 0
                
