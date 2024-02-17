class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        l_c = r_c = added = 0
        for char in s:
            if char=="(":
                l_c += 1
            else:
                if r_c <l_c:
                    r_c += 1
                else:
                    added += 1
        added += l_c - r_c
        return added