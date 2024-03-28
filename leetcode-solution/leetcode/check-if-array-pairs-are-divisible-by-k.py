class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        a = []
        for i in range(len(arr)):
            a.append(arr[i] % k)
        a.sort()
        if a.count(0) % 2 != 0:
            return False
        else:
            i = 0
            while i < len(a) and a[i] == 0:
                i += 1
            j = len(arr) - 1
            while i < j  and (a[j] + a[i]) == k :
                i += 1
                j -= 1
        if i == j + 1:
            return True
        return False

        

        