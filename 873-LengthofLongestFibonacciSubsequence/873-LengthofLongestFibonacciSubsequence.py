class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        result = 0
        n = len(arr)
        s = set(arr)
        # dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1):
            for j in range(i+1, n):
                f1, f2 = arr[i], arr[j]
                curr = 0
                while f1 + f2 in s:
                    curr += 1
                    f1, f2 = f2, f1+f2
                result = max(result, curr)

        return result + 2 if result else 0

        # for i in range(2, n):
        #     target = arr[i]
        #     left, right = 0, i-1
        #     while left < right:
        #         if arr[left] + arr[right] == target:
        #             dp[right][i] = dp[left][right] + 1
        #             result = max(result, dp[right][i])
        #             right -= 1
        #             left += 1
        #         elif arr[left] + arr[right] > target:
        #             right -= 1
        #         elif arr[left] + arr[right] < target:
        #             left += 1

        # return result + 2 if result else 0
                
