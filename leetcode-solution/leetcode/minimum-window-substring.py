class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT = {}
        window = {}
        for t in t:
            countT[t] = 1 + countT.get(t,0)
        have,need = 0,len(countT)
        res = [-1,-1]
        reslen = float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while need == have:
                if (r - l + 1) < reslen:
                    res = [l,r]
                    reslen = (r - l + 1)
                # keep decreasing window size while we still have a valid window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r + 1] if reslen != float("infinity") else ""
            
                
            


            
        