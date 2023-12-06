class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:    
        time_taken=0
        for i in range (len(points)-1):
            time_one = abs(points[i][0]-points[i+1][0])
            time_two = abs(points[i][1]-points[i+1][1])
            time_taken += max(time_one,time_two)
        return time_taken
