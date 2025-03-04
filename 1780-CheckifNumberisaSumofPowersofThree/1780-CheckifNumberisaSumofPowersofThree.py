class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        available = [i for i in range(16)]
        n_a = len(available)
        def dfs(start, path_sum):
            if start > n_a:
                return False

            if path_sum > n:
                return False

            if path_sum == n:
                return True

            for i in range(start, n_a):
                path_sum += pow(3,available[i])
                if dfs(i+1, path_sum):
                    return True
                path_sum -= pow(3,available[i])

            return False

        return dfs(0, 0)
