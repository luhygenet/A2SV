class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.squaresSum(n)
            if n == 1:
                return True
        return False
    def squaresSum(self,n):
        output = 0
        while n != 0:
            dig = n % 10
            output += dig**2
            n = n//10
        return output
