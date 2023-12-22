class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        peak = 0
        for i in range (len(arr)-1):
            if arr[i+1] >arr[i]:
                continue
            else:
                peak = i
                break
        if peak == 0:
            return False
        for i in range (peak+1,len(arr)):
            if arr[i] <arr[i-1]:
                continue
            else:
                return False
        return True

