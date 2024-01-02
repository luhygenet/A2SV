class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        
        maxi = 0
        for i in range(len(points)-1):
            width = points[i+1][0] - points[i][0]
            maxi = max(width,maxi)
        return maxi