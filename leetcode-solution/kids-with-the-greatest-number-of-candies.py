class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bool_of_candies = []
        for i in range (len(candies)):
            most = candies[i] + extraCandies
            for n in range (len(candies)):
                biggest = True
                if most < candies[n]:
                    biggest = False
                    break
            if biggest == True:
                bool_of_candies.append(True)
            else:
                bool_of_candies.append(False)
        return bool_of_candies
