# Last updated: 3/24/2025, 12:42:14 PM
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # sort by start, merge

        meetings.sort(key = lambda x: x[0])
        merged = [meetings[0]]
        n = len(meetings)
        res = meetings[0][0] - 1
        for i in range(1, n):
            curr_meeting = meetings[i]
            if curr_meeting[0] <= merged[-1][1]:
                merged[-1] = [merged[-1][0], max(merged[-1][1], curr_meeting[1])]
            else:
                res += curr_meeting[0] - merged[-1][1] - 1
                merged.append(curr_meeting)
                
        res += days - merged[-1][1]

        return res