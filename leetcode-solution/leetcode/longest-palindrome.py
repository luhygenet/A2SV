class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashi = defaultdict(int)
        for i in range(len(s)):
            hashi[s[i]] += 1
        evens= [x for x in hashi.values() if x % 2 == 0]
        odds = [y for y in hashi.values() if y % 2 != 0]
        if odds:
            can_use = sum(odds) - len(odds) + 1
            return sum(evens) + can_use
        else:
            return sum(evens)
        