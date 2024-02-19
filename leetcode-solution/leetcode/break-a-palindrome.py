class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        paliList = list(palindrome)
        a = palindrome.count("a")
        if n == 1:
            return ""
        for i in range(n):
            if n - a == 1:
                paliList[n - 1] = 'b'
                return "".join(paliList)
            if paliList[i] != 'a':
                paliList[i] = 'a'
                return "".join(paliList)
            if n != 1 and i == n - 1:
                paliList[i] = 'b'
                return "".join(paliList)
        return ""
            
        