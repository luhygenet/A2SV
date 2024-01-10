class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort()
        s.sort()
        i = 0 
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i +=1
            j+=1

        return i

            
        