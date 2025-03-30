# Last updated: 3/30/2025, 2:30:41 PM
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def is_valid(s, t):
            i, j = 0, 0 #s, t

            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1

            return i == len(s)

        letters = set(source)
        targets = set(target)

        for i in target:
            if i not in letters:
                return -1

        result = 1
        concated = source
        while not is_valid(target, concated):
            concated += source
            result += 1

        return result

        

