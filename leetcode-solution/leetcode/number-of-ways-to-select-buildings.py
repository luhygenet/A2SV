class Solution:
    def numberOfWays(self, s: str) -> int:
        hashi = { "0" : 0, "1" : 0, "01" : 0, "10" : 0}
        hashi[s[0]] += 1
        res = 0
        for i in range(1,len(s)):
            hashi[s[i]] += 1
            if s[i] == "0":
                hashi["10"] += hashi["1"]
                res += hashi["01"]
            else:
                hashi["01"] += hashi["0"]
                res += hashi["10"]
        return res
            


                    




