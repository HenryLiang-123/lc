class Solution:
    def coloredCells(self, n: int) -> int:
        
        square = pow(2*n - 1, 2)
        missing = n*n - ((n + 1) * n) / 2

        return int(square - missing * 4)