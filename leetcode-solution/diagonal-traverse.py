class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n =len(mat[0])
        if n  == 0 or m == 0:
            return []
        new_arr = []
        row, col = 0,  0
        up = True
        
        while row < m and col < n:
            new_arr.append(mat[row][col])
            if up:
                while row > 0 and col < n-1:
                    row-=1
                    col+=1
                    new_arr.append(mat[row][col])                   
         

                if col == n-1:
                    row+=1
                else:
                    col+=1
            else:
                while row < m-1 and col > 0:
                    row+=1
                    col-=1
                    new_arr.append(mat[row][col])                  
                    
                
                if row == m-1:
                    col+=1
                else:
                    row+=1
            up = not up

        return new_arr 

