class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        
        hour_sum = 0
        for x in range (1, r-1):
            for y in range(1,c-1):
                total = 0
                for dx in range(-1,2):
                    for dy in range(-1,2):
                         total += grid[x+dx][y+dy]
                total -= grid[x][y-1]
                total -= grid[x][y+1]

                hour_sum =max(hour_sum,total)
        return hour_sum
