class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n_s = len(s)
        n_part = len(part)
        stack = []
        for i in range(n_s):
            stack.append(s[i])
            
            if len(stack) >= n_part and "".join(stack[-n_part:]) == part:
                for _ in range(n_part):
                    stack.pop()

        return "".join(stack)