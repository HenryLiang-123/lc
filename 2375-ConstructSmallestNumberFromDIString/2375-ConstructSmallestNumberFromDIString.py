// Last updated: 2/18/2025, 12:56:25 PM
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        stack = []
        n = len(pattern)

        for i in range(n + 1):
            stack.append(i+1)

            if i == n or pattern[i] == "I":
                while stack:
                    result.append(str(stack.pop()))

        return "".join(result)
        # counts = {str(i):1 for i in range(1, 10)}
        # n = len(pattern) + 1
        # result = []
        # def dfs(i, path):
        #     if i == n:
        #         result.append(path[:])
        #         return True
            
        #     if i > n:
        #         return False

        #     for choice, _ in counts.items():
        #         if i == 0:
        #             path.append(choice)
        #             counts[choice] -= 1
        #             if dfs(i+1, path):
        #                 return True
        #             path.pop()
        #             counts[choice] += 1
        #         else:
        #             curr_pattern = pattern[i-1]
        #             if curr_pattern == "I":
        #                 if counts[choice] > 0 and path[-1] < choice:
        #                     path.append(choice)
        #                     counts[choice] -= 1
        #                     if dfs(i+1, path):
        #                         return True
        #                     path.pop()
        #                     counts[choice] += 1
        #             else:
        #                 if counts[choice] > 0 and path[-1] > choice:
        #                     path.append(choice)
        #                     counts[choice] -= 1
        #                     if dfs(i+1, path):
        #                         return True
        #                     path.pop()
        #                     counts[choice] += 1
        #     return False
        # dfs(0, [])
        # return "".join(result[0])

