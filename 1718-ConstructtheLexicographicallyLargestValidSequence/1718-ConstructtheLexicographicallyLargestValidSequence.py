// Last updated: 2/28/2025, 3:57:17 PM
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        seen = set()
        choices = [i for i in reversed(range(1, n+1))]
        print(choices)
        slots = 2 * (n-1) + 1
        result = [0 for _ in range(slots)]
        def dfs(i):
            if i >= slots:
                return True

            for c in choices:
                if c in seen:
                    continue
                if c > 1:
                    if i + c >= slots or result[i] > 0 or result[i+c] > 0:
                        continue
                else:
                    if result[i] > 0:
                        continue
                
                result[i] = c
                if c > 1:
                    result[i+c] = c
                seen.add(c)

                next_slot = i
                while next_slot < slots and result[next_slot]:
                    next_slot += 1

                if dfs(next_slot):
                    return True

                result[i] = 0
                if c > 1:
                    result[i+c] = 0
                seen.remove(c)

            return False

        dfs(0)
        return (result)

