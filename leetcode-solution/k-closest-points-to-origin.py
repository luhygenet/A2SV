class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxi = 0
        li=[]
        def comparator(points):
            return (points[0]**2+(points[1]**2))
        
        points.sort(key = comparator)
        i = 0 
        while i < len(points) and len(li) < k:
            li.append(points[i])
            i+=1
        return li
        



        
