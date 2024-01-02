class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxi = 0
        count = 0
        pref_al = 0
        
        for i in range (len(flips)):
            maxi = max(maxi, flips[i])
            count += 1
            print(maxi, count) 
            if count == maxi:
                pref_al += 1 
                
        return pref_al
