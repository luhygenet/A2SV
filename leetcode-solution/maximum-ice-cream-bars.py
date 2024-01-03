class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxi = max(costs)
        res= [0] *(maxi+1)
        fin =[]
        count = 0
        for i in range(len(costs)):
            res[costs[i]] +=1
        for i in range(len(res)):
            for j in range(res[i]):
                fin.append(i)
        print(fin)

        for i in range(len(fin)):
           count += fin[i]
           if count > coins:
               return i
           elif fin[0] > coins:
               return 0
        return len(fin)
           