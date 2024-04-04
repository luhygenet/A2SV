class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        directions = [(1,0),(-1,0),(0, 1),(0, -1)]
        visited = set()
        def isbound(row,col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == '0':
                return False
            else:
                return True

        def dfs(row, col):
            if (row,col) in visited or not isbound(row,col):
                return False

            visited.add((row,col))


            for nex_row,nex_col in directions:
                new_r = nex_row + row
                new_c = nex_col + col
                
                dfs(new_r,new_c)
            

        res = 0
        for i in range(rows):
            for j in range(cols):
                if int(grid[i][j]) and (i,j) not in visited:
                    res += 1
                    dfs(i,j)
                    
        return res
        

       