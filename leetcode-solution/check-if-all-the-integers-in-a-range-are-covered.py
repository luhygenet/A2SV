class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        sets =set()
        for i in ranges:
            start = i[0]
            end = i[1]
            for j in range (start,end+1):
                sets.add(j)
        for i in range (left, right+1):
            if i not in sets:
                return False
        return True
            