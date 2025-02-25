// Last updated: 2/24/2025, 8:27:09 PM
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        slots = 2 * (n-1) + 1
        result = [0 for _ in range(slots)]
        choices = [i for i in reversed(range(1, n+1))]
        print(choices)
        seen = set()
        def dfs(idx):
            if idx == slots:
                return True

            for c in choices:
                if c in seen:
                    continue
                # print(idx + c)
                if c > 1 and (idx + c >= len(result) or result[idx+c] > 0):
                    continue

                seen.add(c)
                result[idx] = c
                if c > 1:
                    result[idx + c] = c

                next_spot = idx + 1
                while next_spot < len(result) and result[next_spot]:
                    next_spot += 1

                if dfs(next_spot):
                    return True

                seen.remove(c)
                result[idx] = 0
                if c > 1:
                    result[idx + c] = 0
            
            return False

        dfs(0)
        return (result)
                

                





