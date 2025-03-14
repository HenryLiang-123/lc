class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1

        result = []

        while left <= right and top <= bottom:

            #top:
            for i in range(left, right+1):
                result.append(matrix[top][i])
            
            top += 1

            #down:
            for i in range(top, bottom+1):
                result.append(matrix[i][right])

            right -= 1

            #bottom:
            if bottom >= top:
                for i in reversed(range(left, right+1)):
                    result.append(matrix[bottom][i])
                
                bottom -= 1

            #up:
            if right >= left:
                for i in reversed(range(top, bottom+1)):
                    result.append(matrix[i][left])

                left += 1

            print(result, left, right, top, bottom)

        return result