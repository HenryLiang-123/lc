class Solution:
    def numDecodings(self, s: str) -> int:
        valid = set([str(i) for i in range(1,27)])
        n = len(s)
        dp = [0 for _ in range(n)]
        dp[0] = 1 if s[0] in valid else 0

        if n == 1:
            return dp[-1]

        if s[1] in valid and dp[0]:
            dp[1] += 1
        
        if s[0:2] in valid:
            dp[1] += 1

        for i in range(2, n):
            curr = s[i]
            
            if s[i] in valid and dp[i-1]:
                dp[i] += dp[i-1]

            # print(s[i-1:i+1])
            if s[i-1:(i+1)] in valid:
                dp[i] += dp[i-2]

        return dp[-1]
