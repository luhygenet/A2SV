class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            a = sums + i
            b = i + 1
            comp = a//b
            ans = max(comp,ans)
        return ans