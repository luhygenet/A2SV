class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seti = {}
        res = 0

        l = 0
        for r in range(len(s)):
            seti[s[r]] = 1 + seti.get(s[r], 0)
            while(r-l+1) -max(seti.values()) > k:
                seti[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
            