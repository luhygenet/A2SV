class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:        
        size =len(heights)
        names.reverse()
        heights.reverse()
        print(names)

        
        for i in range(len(heights)):
            mini = i
            for j in range(i+1,size):
                if heights[j] > heights[mini]:
                    mini = j 
            heights[i],heights[mini] = heights[mini],heights[i] 
            names[i],names[mini] = names[mini],names[i] 
        return names


