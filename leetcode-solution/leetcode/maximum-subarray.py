class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float(-inf)
        n = len(nums)
        pref = 0
        for i in range(len(nums)):
            pref += nums[i]
            ans = max(ans,pref)
            if pref < 0:
                pref = 0
            
        return  ans
