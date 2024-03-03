class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairs = [0] * (n - 1)
        for i in range(1,n):
            pairs[i - 1] = weights[i] + weights[i - 1]
        pairs.sort()
        mini = 0
        maxi = 0
        for i in range(k-1):
            mini += pairs[i]
            maxi += pairs[n-i-2]
        return maxi - mini

