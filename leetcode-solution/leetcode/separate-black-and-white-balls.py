class Solution:
    def minimumSteps(self, s: str) -> int:
        j = len(s) - 1
        i = 0
        swaps = 0
        while i < j:
            while j > 0 and s[j] == '1':
                j -= 1
            while i < len(s) and s[i] == '0':
                i += 1
            if j - i < 0:
                break
            swaps += j - i
            i += 1
            j -= 1
        return swaps
        
            
            

            
        




