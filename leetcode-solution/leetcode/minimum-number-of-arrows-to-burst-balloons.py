class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:return 0
        points.sort()
        count = 1
        prev = points[0]
        for start,end in points[1:]:
            if start > prev[1]:
                prev = [start,end]
                count += 1
            else:
                prev[1] = min(prev[1],end)
        return count




