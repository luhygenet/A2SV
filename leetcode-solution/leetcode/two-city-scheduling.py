class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        final = []
        for i in range(len(costs)):
            new = [0,0,0]
            new[0] = costs[i][1] - costs[i][0]
            new[1] = costs[i][1]
            new[2] = costs[i][0]
            final.append(new)
        final.sort()
        saved = 0
        for i in range(len(final)):
            if i < len(final)//2:
                saved += final[i][1]
            else:
                saved += final[i][2]
        return saved





