class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        seen = set()
        choices = [i for i in reversed(range(1, n+1))]
        result = [0 for _ in range((n-1)*2 +1)]

        def dfs(idx):
            # nonlocal result
            if idx == len(result):
                # we've filled it out
                return True

            for c in reversed(range(1, n+1)):
                # if we've used the current choice or if the space is occupied, we try next
                if c in seen:
                    continue
                if c > 1 and (idx + c >= len(result) or result[idx+c] > 0):
                    continue
                
                # use curr element
                seen.add(c)
                result[idx] = c
                if c > 1:
                    result[idx+c] = c

                # next spot
                next_spot = idx + 1
                while next_spot < len(result) and result[next_spot]:
                    next_spot += 1

                if dfs(next_spot):
                    return True

                seen.remove(c)
                result[idx] = 0
                if c > 1:
                    result[idx+c] = 0

            return False

        dfs(0)


            

        return result
            

            

            