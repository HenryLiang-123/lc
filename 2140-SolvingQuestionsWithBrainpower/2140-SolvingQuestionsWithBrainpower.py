# Last updated: 4/1/2025, 4:39:37 PM
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [float('-inf') for _ in range(n)]
        dp[-1] = questions[-1][0]

        for i in range(n-2, -1, -1):
            next_available_idx = i + questions[i][1] + 1
            if next_available_idx >= n:
                to_add = 0
            else:
                to_add = dp[next_available_idx]
            dp[i] = max(dp[i+1], to_add + questions[i][0])

        return dp[0]