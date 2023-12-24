class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        def flip(row):
            for i in range(len(row)):
                row[i] = 1 - row[i]
                
            return row

        for i in range(len(image)):
            image[i] = flip(image[i][::-1])

        return image
