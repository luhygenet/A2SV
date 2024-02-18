class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        curr = 0
        pref = {}
        pref[0] = -1
        best = (float('inf'))
        for i, x in enumerate(nums):
            curr += x
            curr %= p
            if ((curr - target) % p) in pref:
                best = min(i - pref[(curr - target) % p],best)    
            pref[curr] = i
            
        if best >= len(nums):
            return -1
        return best


       

