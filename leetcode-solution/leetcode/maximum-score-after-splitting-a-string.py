class Solution:
    def maxScore(self, s: str) -> int:
        sumOne = 0
        maxScore = 0
        for i in range(len(s)):
            sumOne += int(s[i])
        sumZero = 0
        for i in range(len(s)- 1):
            if s[i] == "0":
                sumZero += 1
            else:
                sumZero -= 1
            maxScore = max(maxScore, sumZero + sumOne)
        return maxScore


