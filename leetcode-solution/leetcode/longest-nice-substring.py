class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def half(s):
            if len(s) < 2:
                return ""
            seti = set(s)
            for i,w in enumerate(s):
                if w.swapcase() not in seti:
                    s1 = half(s[0:i])
                    s2 = half(s[i+1:])
                    return s2 if len(s2) > len(s1) else s1
            return s
        return half(s)

