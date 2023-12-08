class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        new = []
        
        for i in range (len(boxes)):
            sums = 0
            for j in range (len(boxes)):
                if boxes[j]  == "1":
                    sums += abs(i -j) 
            new.append(sums)
        return new
            
             