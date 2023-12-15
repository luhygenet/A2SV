class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        occuring_number = (len(arr)*25)/100
        count = 1
        i = 0
        j = i + 1
        while j < len(arr): 
            if arr[i] != arr[j]:
                i = j
                j +=1
                count = 1
            else:
                j +=1
                count +=1
                if count > occuring_number:
                    break

        return arr[i]
