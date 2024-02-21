class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1] * (rowIndex + 1)
        previous_row = self.getRow(rowIndex - 1)
        curr = [1]
        for i in range(len(previous_row) - 1):
            curr.append(previous_row[i] + previous_row[i+1])
        curr.append(1)
        return curr

