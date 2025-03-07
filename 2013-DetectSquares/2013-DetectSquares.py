// Last updated: 3/6/2025, 9:18:21 PM
class DetectSquares:

    def __init__(self):
        self.point_to_freq = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        # point = (point[0], point[1])
        self.point_to_freq[tuple(point)] += 1
        
    def count(self, point: List[int]) -> int:
        # go thru all points, assuming that point is the diag
        result = 0
        x1, y1 = point
        for diagonal in self.point_to_freq:

            x2, y2 = diagonal
            if (x1, y2) in self.point_to_freq and (x2, y1) in self.point_to_freq and tuple(point) != diagonal and abs(x1-x2) == abs(y1-y2):
                result += self.point_to_freq[(x1,y2)] * self.point_to_freq[(x2,y1)] * self.point_to_freq[diagonal]

        return result



        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)