class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)//2
        memo = {}
        def dp(i,tar):
            if i >= len(nums) or tar <= 0:
                return tar == 0

            now = (i,tar)
            if now not in memo:
                memo[now] = dp(i + 1, tar - nums[i]) or dp(i + 1, tar)
            return memo[now]
        return dp(0,target)
            
            