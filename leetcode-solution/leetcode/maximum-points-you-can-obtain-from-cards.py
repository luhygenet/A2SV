class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        r = 0
        l = 0
        sumi = 0
        maxi = 0
        for i in range(n - k):
            r += 1
        for i in range(r,n):
            sumi += cardPoints[i]
        maxi = max(maxi,sumi)
        print(maxi)
        for i in range(n-k,n):
            print(i)
            print(maxi)
            sumi-=cardPoints[i]
            sumi+=cardPoints[l]
            maxi = max(maxi,sumi)
            l += 1
        return maxi

            
            
        


