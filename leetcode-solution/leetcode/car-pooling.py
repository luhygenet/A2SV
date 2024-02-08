class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pref = [0] * 1001

        for passengs,_from,_to in trips:
            pref[_from] += passengs
            pref[_to] -= passengs
        for i in range(1,1001):
            pref[i] += pref[i-1]
            
            if pref[i] > capacity:
                return False
        if pref[0] > capacity:
            return False
        return True

        
