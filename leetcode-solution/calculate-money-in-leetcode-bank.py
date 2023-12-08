class Solution:
    def totalMoney(self, n: int) -> int:
        count = 0
        result = 0
        monday = 1

        for _ in range(n):
            if count == 7:
                monday += 1
                count = 0 

            result += (monday + count)
            count += 1
            
        return result


        