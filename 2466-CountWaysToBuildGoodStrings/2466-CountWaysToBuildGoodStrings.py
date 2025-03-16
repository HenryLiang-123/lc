class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        memo = {}
        MOD = 10**9 + 7
        def dfs(path_len):
            if path_len in memo:
                return memo[path_len]

            result = 0
            if low <= path_len <= high:
                result += 1

            if path_len > high:
                return 0

            add_zero = dfs(path_len + zero)
            add_one = dfs(path_len + one)

            memo[path_len] = (result + add_zero + add_one) % MOD

            return memo[path_len]

        return dfs(0)