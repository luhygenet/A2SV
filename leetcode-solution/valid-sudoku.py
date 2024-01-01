class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        c = collections.defaultdict(set)
        r = collections.defaultdict(set)
        sqr = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] ==".":
                    continue
                if (board[i][j] in r[i] or 
                    board[i][j] in c[j] or
                    board[i][j] in sqr[(i//3, j//3)]):
                    return False
                c[j].add(board[i][j])
                r[i].add(board[i][j])
                sqr[(i//3, j//3)].add(board[i][j])
        return True

                


