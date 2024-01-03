class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count = 0
        j = len(piles)
        for i in range((len(piles)//3)):
            print(j)
            j-=2
            m = j
            count += piles[m]
        return count
            


