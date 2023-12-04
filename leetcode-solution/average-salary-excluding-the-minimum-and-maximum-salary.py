class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary=salary[1:-1]
        sum = 0
        for i in salary:
            sum += i
        sum = sum/len(salary)
        return sum