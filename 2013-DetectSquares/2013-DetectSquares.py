class DetectSquares:

    def __init__(self):
        self.point_to_freq = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.point_to_freq[tuple(point)] += 1
    
    def count(self, point: List[int]) -> int:
        x, y = point
        result = 0
        for diag in self.point_to_freq:
            if abs(diag[0] - x) != abs(diag[1] - y) or (x == diag[0] and y == diag[1]):
                continue

            top = (diag[0], y)
            right = (x, diag[1])

            if top in self.point_to_freq and right in self.point_to_freq:
                result += self.point_to_freq[diag] * self.point_to_freq[top] * self.point_to_freq[right]

        return result
                
                
                


        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)