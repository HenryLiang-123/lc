# Last updated: 3/30/2025, 1:33:19 PM
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        result = []
        start = 0
        end = s.rindex(s[0])
        for i in range(1, n):
            letter = s[i]
            first, last = s.index(letter), s.rindex(letter)
            if first < end:
                end = max(end, last)
            else:
                result.append(end - start + 1)
                start = first
                end = last

        if end - start + 1 > 0:
            result.append(end-start+1)

        return result


            




        