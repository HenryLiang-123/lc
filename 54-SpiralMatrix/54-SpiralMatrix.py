// Last updated: 3/13/2025, 11:54:16 PM
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)

        result = []

        while left < right and top < bottom:

            #top:
            for i in range(left, right):
                result.append(matrix[top][i])
            
            top += 1

            #down:
            for i in range(top, bottom):
                result.append(matrix[i][right-1])

            right -= 1

            #bottom:
            if bottom > top:
                for i in reversed(range(left, right)):
                    result.append(matrix[bottom-1][i])
                
                bottom -= 1

            #up:
            if right > left:
                for i in reversed(range(top, bottom)):
                    result.append(matrix[i][left])

                left += 1


        return result