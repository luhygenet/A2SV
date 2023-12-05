class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        total_steps = 0
        x=-1
        initial = capacity
        i=0
        while i<len(plants):
            if plants[x+1] > capacity:
                total_steps += (x)*2 + 3    
                capacity = initial
                capacity -= plants[i]
            else:
                total_steps += 1
                capacity -= plants[x+1]
            x +=1
            i +=1
        return total_steps    

            