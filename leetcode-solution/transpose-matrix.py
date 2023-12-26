class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        row, cols =len(matrix), len(matrix[0])
        res = [[0]*row for i in range(cols)]
        
        for i in range (row):
            for j in range(cols):
                res[j][i] = matrix[i][j]
        return res