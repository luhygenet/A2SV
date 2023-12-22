class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        N = len(matrix)
        for row in range(N):
            for col in range(row, N):
                matrix[row][col], matrix[col][row] =  matrix[col][row], matrix[row][col]

        
        print(matrix)
        def reverse(row):
            left = 0
            right = N - 1
            while left < right:
                matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]   
                left += 1
                right -= 1
        
        for row in range(N):
            reverse(row)

