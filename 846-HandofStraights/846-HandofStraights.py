import heapq
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)
        starts = list(counts.keys())
        heapq.heapify(starts)

        while starts:
            s = starts[0]
            if counts[s] == 0:
                heapq.heappop(starts)
                continue
            for i in range(s, s + groupSize):
                if i not in counts:
                    print("first",i)
                    return False
                if counts[i] - 1 < 0:
                    print(i)
                    print("second",counts[i])
                    return False
                counts[i] -= 1

            

        return True