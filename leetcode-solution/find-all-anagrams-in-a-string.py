class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = defaultdict(int)
        window = defaultdict(int)
        res = []
        if len(p) > len(s):
            return res
        for i in range (len(p)):
            target[p[i]] += 1
            window[s[i]] += 1
        i = 0
        for j in range(len(p),len(s)):
            if target == window:
                res.append(i)
            window[s[i]] -=1
            if window[s[i]] == 0:
                del(window[s[i]])
            window[s[j]] +=1
            i+=1
        if target == window:
                res.append(i)
        return res
        

        

            

                