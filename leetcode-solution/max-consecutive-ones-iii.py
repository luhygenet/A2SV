class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        maxi = 0
        [1,1,1,0,0,0,1,1,1,1,0]
        

        for r,n in enumerate(nums):
            k -= (1-n)
            if k < 0:
                k+=(1-nums[l])
                l += 1
            maxi = max(maxi, r - l +1)
        return maxi