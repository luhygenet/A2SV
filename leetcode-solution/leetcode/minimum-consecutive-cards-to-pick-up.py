class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mini = float('inf')
        l = 0
        cons = {}
        j = 0 
        for r,n in enumerate(cards):
            if n in cons:
                mini = min(mini,r - cons[n] + 1)
            cons[n] = r
        if mini == float('inf'): return -1
        return mini
                
