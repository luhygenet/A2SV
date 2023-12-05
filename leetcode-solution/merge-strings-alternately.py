class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        total=[]
        i=0
        j=0
        while i < len(word1) and j < len(word2):
            total.append(word1[i])
            total.append(word2[j])
            i+=1
            j+=1
        total.append(word1[i:])
        total.append(word2[j:])
        return "".join(total)