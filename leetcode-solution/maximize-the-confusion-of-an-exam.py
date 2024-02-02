class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        best = 0

        for correct in ["T","F"]:
            count = 0
            l = 0
            for r in range(n):
                if answerKey[r] != correct:
                    count += 1
                while count > k:
                    if answerKey[l] != correct:
                        count -= 1
                    l += 1
                best = max(best,r - l + 1)
        return best

         