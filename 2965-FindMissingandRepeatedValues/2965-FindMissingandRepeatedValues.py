class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        h = {i:0 for i in range(1, n*n+1)}
        elements = []
        for i in range(n):
            for j in range(n):
                elements.append(grid[i][j])

        for e in elements:
            h[e] += 1

        a = [key for key, value in h.items() if value > 1]
        b = [key for key, value in h.items() if value == 0]

        return [a[0], b[0]]