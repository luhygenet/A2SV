class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        minmax = 0
        n =len(grid)
        res = [[0]*n for i in range(n)]
        final = [[0]*n for i in range(n)]
        
        for i in range (n):
            for j in range(n):
                res[j][i] = grid[i][j]
        for i in range(n):
            col = max(grid[i])
            for j in range(n):
                final[i][j] = min(max(res[j]),col)
        maxi = 0
        for i in range(n):
            for j in range(n):
                maxi += final[i][j] - grid[i][j] 
        return(maxi)
       
                
