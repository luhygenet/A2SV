class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        red = set()
        row = len(board)
        col = len(board[0])
        def bt(r,c,i):
            if i == len(word):
                return True
            if (c<0 or r<0  or c>=col or r >=row or (r,c) in red  or word[i]!=board[r][c]):
                return False
            red.add((r,c))
            res = (bt(r + 1,c, i+1) or
                  bt(r - 1,c, i+1)or
                  bt(r ,c+ 1, i+1)or
                  bt(r,c-1, i+1))
            red.remove((r,c))
            return res
        for r in range(row):
            for c in range(col):
                if bt(r,c,0): return True
        return False
        
            
            


