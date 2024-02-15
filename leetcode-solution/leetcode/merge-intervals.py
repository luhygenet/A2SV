class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x : x[0])
        new = [intervals[0]]
        for start,end in intervals[1:]:
            lastE = new[-1][1]
            if start <= lastE:
                new[-1][1] = max(lastE, end)
            else:
                new.append([start,end]) 
        return new