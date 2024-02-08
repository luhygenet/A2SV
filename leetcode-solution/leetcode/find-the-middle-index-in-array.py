class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        cur = 0
        tot = sum(nums)
        for i in range(n):
            cur += nums[i]
            if cur - nums[i] == tot - cur:
                return i
        return -1