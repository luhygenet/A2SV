class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = {}
        l = 0
        maxi = 0
        output = 0
        for i,n in enumerate(nums):
            if n in seen:
                while l < seen[n] + 1:
                    maxi -= nums[l]
                    l += 1
            seen[n] = i
            maxi += n
            output = max(maxi,output)
        return output
            
            