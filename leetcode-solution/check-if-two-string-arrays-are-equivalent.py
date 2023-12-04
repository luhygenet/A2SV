class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        full=""
        tfull=""
        for i in word1:
            full+=i
        for i in word2:
            tfull+=i
        if full == tfull:
            return True
        else:
            return False
        