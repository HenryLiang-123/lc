class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        memo = {}
        def dfs(choices, remainder):
            if choices[-1] >= remainder:
                return True

            key = tuple(choices)
            if (key, remainder) in memo:
                return memo[(key, remainder)]
            
            for i in range(len(choices)):
                new_choices = choices[:i] + choices[(i+1):]
                if not dfs(new_choices, remainder - choices[i]):
                    memo[(key, remainder)] = True
                    return True

            memo[(key, remainder)] = False
            return memo[(key, remainder)]

        choices = [x for x in range(1, maxChoosableInteger + 1)]

        if maxChoosableInteger >= desiredTotal:
            return True

        if sum(choices) < desiredTotal:
            return False

        return dfs(choices, desiredTotal)
