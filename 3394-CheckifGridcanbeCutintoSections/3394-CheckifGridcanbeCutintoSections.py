# Last updated: 3/25/2025, 3:21:06 PM
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # merge vertically and merge (full merge) horizontally. If 3, good.
        vertical = []
        horizontal = []
        for start_x, start_y, end_x, end_y in rectangles:
            curr_h = [start_y, end_y]
            curr_v = [start_x, end_x]
            vertical.append(curr_v)
            horizontal.append(curr_h)

        def merge(intervals):
            intervals.sort(key = lambda x: x[0])
            merged = [intervals[0]]

            for i in range(1, len(intervals)):
                prev = merged[-1]
                curr = intervals[i]
                if curr[0] < prev[1]:
                    merged[-1] = [prev[0], max(prev[1], curr[1])]
                else:
                    merged.append(curr)

            return merged

        return len(merge(horizontal)) >= 3 or  len(merge(vertical)) >= 3


