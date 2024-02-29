class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        hashi = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz"}
        final = []
        word = []
        def bt(j):
            if  j >= len(digits):
                n = "".join(word)
                final.append(n)
                return 
            for i in range(len(hashi[digits[j]])):
                word.append(hashi[digits[j]][i])
                bt(j+1)
                word.pop()
        bt(0)
        return final
            

            