class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vset = set('aeiou')
        count = 0
        for i in range(k):
            if s[i] in vset:
                count += 1
        l = 0
        r = k - 1
        maxi = count
        while r < len(s) - 1:
            if s[l] in vset:
                count -= 1
            l += 1
            r += 1
            if s[r] in vset:
                count += 1
            maxi = max(maxi, count)
        return maxi
