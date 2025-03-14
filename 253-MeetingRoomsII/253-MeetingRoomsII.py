// Last updated: 3/14/2025, 6:19:17 PM
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([x[0] for x in intervals])
        ends = sorted([x[1] for x in intervals])
        n = len(starts)
        rooms = 0
        e = 0
        for s in range(n):
            rooms += 1
            if starts[s] >= ends[e]:
                rooms -= 1
                e += 1

        return rooms

