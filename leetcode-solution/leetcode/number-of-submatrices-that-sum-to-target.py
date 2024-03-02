class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        mat2 = [[0]*cols for i in range(rows)]
        for r in range(rows):
            for c in range(cols):
                top = mat2[r-1][c] if r>0 else 0
                left = mat2[r][c-1] if c>0 else 0
                top_left = mat2[r-1][c-1] if r > 0 and c > 0 else 0
                mat2[r][c] += matrix[r][c] + top + left - top_left
        res = 0
        for r1 in range(rows):
            for r2 in range(r1,rows):
                counts = defaultdict(int)
                counts[0] = 1
                for c in range(cols):
                    curr_sum = mat2[r2][c] - (mat2[r1-1][c] if r1 > 0 else 0)
                    diff = curr_sum - target
                    res += counts[diff]
                    counts[curr_sum] += 1
        return res

        
