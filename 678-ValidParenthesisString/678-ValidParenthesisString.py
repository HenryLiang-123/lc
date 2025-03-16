// Last updated: 3/16/2025, 2:06:59 PM
class Solution:
    def checkValidString(self, s: str) -> bool:
        # close left when we have a right
        # if we can't, try to close with star
        # if we can't false

        # at the end, there may be left over lefts.
        # if the stars appear after, we can close. Else, False

        left_stack = [] #idx
        star_stack = [] #idx

        n = len(s)

        for i in range(n):
            if s[i] == "(":
                left_stack.append(i)
            elif s[i] == "*":
                star_stack.append(i)
            else:
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        if not left_stack:
            return True

        if len(left_stack) > len(star_stack):
            return False

        while left_stack:
            left_idx = left_stack.pop()
            star_idx = star_stack.pop()
            
            if left_idx > star_idx:
                return False


        return True

