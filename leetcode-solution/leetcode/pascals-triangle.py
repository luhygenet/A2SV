class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]  
        previous_row = self.generate(numRows-1)
        curr = [1]
        for i in range(len(previous_row[-1]) - 1):
            curr.append(previous_row[-1][i] + previous_row[-1][i + 1])
        curr.append(1)
        previous_row.append(curr)
        return previous_row
        


        