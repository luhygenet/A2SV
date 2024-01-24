class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        long = 0
        l = 0
        r = 0
        curr = 0

        while r < len(nums):
            if nums[r] == 0:
                curr += 1
            while curr > 1:
                if nums[l] == 0:
                    curr -= 1
                l += 1
            r += 1
            long = max(long,r - l - 1)
        return long

            