class Solution:
    def isValid(self, s: str) -> bool:
        sta = []
        hashi = {'}':'{', ']':'[', ')':'('}
        if s[0] in hashi:
            return False
        for i in range(len(s)):
            if s[i] in hashi:
                if sta and sta[- 1] == hashi[s[i]]:
                    sta.pop()
                else:
                    return False
            else:
                sta.append(s[i])
        if not sta:
            return True
        return False