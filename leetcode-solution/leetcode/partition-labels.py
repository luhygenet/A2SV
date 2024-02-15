class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashi = {}
        out = []
        for i in range(len(s)):
            if s[i] in hashi and hashi[s[i]] < i:
                hashi[s[i]] = i
            else:
                hashi[s[i]] = i
        length = 0
        end = 0 
        for i in range(len(s)):
            length += 1
            end = max(end,hashi[s[i]])
            if i == end:
                out.append(length)
                length = 0
        return out

            


    
        