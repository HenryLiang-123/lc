class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)

        dp = [[False for _ in range(n+1)] for _ in range(m+1)]

        dp[0][0] = True

        if n + m != len(s3):
            return False

        if n == 0 or m == 0:
            return s1==s3 or s2==s3

        for i in range(1, n+1):
            if s1[i-1] == s3[i-1] and dp[0][i-1]:
                dp[0][i] = True

        print(dp)

        for i in range(1, m+1):
            print(i, s2[i-1],s3[i-1], dp[i-1][0])
            if s2[i-1] == s3[i-1] and dp[i-1][0]:
                dp[i][0] = True

        for i in range(1, m+1):
            for j in range(1, n+1):
                if dp[i-1][j] and s2[i-1] == s3[i+j-1]:
                    dp[i][j] = True

                if dp[i][j-1] and s1[j-1] == s3[i+j-1]:
                    dp[i][j] = True

        print(dp)
        return dp[-1][-1]