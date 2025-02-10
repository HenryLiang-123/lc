from collections import deque
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = deque([])
        n = len(s)
        for i in range(n):
            if not s[i].isdigit():
                stack.append(s[i])
            else:
                stack.pop()

        return "".join(stack)