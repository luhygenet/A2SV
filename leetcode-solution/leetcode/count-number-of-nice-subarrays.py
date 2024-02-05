class Solution: 
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        odd = 0
        cnt = 0
        l = 0
        r = 0
        while r < n:
            if nums[r]%2 != 0:
                odd += 1
                cnt = 0
            while odd == k:
                cnt += 1
                odd -= nums[l] & 1
                l += 1
            ans += cnt
            r += 1
        return ans
