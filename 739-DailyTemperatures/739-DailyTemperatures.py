class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        stack.append((temperatures[0], 0)) #temp, time
        n = len(temperatures)
        result = [0 for _ in range(n)]
        for i in range(1, n):
            curr = temperatures[i]
            while stack and stack[-1][0] < curr:
                _, time = stack.pop()
                result[time] = i - time
            stack.append((curr, i))

        return result

