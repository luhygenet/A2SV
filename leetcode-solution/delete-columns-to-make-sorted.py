class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for n in range (len(strs[0])):
            m = 0
            while m < len(strs)-1 :
                if strs[m][n] > strs[m+1][n]:
                    count+=1
                    break
                m +=1
        return count
        