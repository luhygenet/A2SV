class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i,j = 0,0
        n,m = len(firstList),len(secondList)
        output = []
        while (i < n and j < m):
            start = max(firstList[i][0],secondList[j][0])
            end = min(firstList[i][1],secondList[j][1])

            if start <= end:
                output.append([start,end])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return output
        