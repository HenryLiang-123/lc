from collections import deque
class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = deque([])
        star_stack = deque([])

        n = len(s)

        for i in range(n):
            curr = s[i]
            if curr == "(":
                left_stack.append(i)
            elif curr == "*":
                star_stack.append(i)
            else:
                # curr = ')'
                if left_stack:
                    left_stack.pop()
                elif not left_stack and star_stack:
                    star_stack.pop()
                elif not left_stack and not star_stack:
                    return False
        print(left_stack, star_stack)
        if left_stack:
            if len(left_stack) > len(star_stack):
                return False
            else:
                while left_stack:
                    left_top = left_stack.pop()
                    star_top = star_stack.pop()
                    if left_top > star_top:
                        return False

        return True