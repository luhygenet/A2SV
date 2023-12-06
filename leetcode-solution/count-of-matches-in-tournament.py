class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        match_total = 0
        while n != 1:
            if n % 2 == 0:
                matches = n/2
                match_total += matches
                n = n/2
            else:
                matches = (n -1)/2 
                match_total += matches
                n = ((n-1)/2) + 1
        return int(match_total)

