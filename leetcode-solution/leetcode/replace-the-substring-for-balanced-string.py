class Solution:
    def balancedString(self, s: str) -> int:
        hashi = defaultdict(int)
        res = len(s)
        for i in s:
            hashi[i] += 1
        print(hashi)
        l = 0
        for r in range(len(s)):
            hashi[s[r]] -= 1
            while l < len(s) and all(hashi[c] <= len(s)//4 for c in 'QWER') :
                res = min(res,r-l+1)
                hashi[s[l]] += 1
                l += 1
        return res 
        

            
                
