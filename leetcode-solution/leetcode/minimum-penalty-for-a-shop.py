class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        currSum = mini = customers.count('Y')
        res = -1
        for i,ch in enumerate(customers):
            if ch =="Y":
                currSum -= 1
            else:
                currSum += 1
            if currSum < mini:
                mini = currSum
                res = i
        return res + 1
            


