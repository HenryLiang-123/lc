class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def lcs(s1, s2):
            n = len(s1)
            m = len(s2)
            dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            result = []
            s1_idx = []
            s2_idx = []
            i, j = n, m
            while i > 0 and j > 0:
                if s1[i-1] == s2[j-1]:
                    result.append(s1[i-1])
                    i -= 1
                    j -= 1
                elif dp[i][j-1] > dp[i-1][j]:
                    result.append(s2[j-1])
                    j -= 1
                else:
                    result.append(s1[i-1])
                    i -= 1

            if i > 0:
                result.append(s1[0:i])
            if j > 0:
                result.append(s2[0:j])
            return "".join(result[::-1])

        return (lcs(str1, str2))

      




                    





        