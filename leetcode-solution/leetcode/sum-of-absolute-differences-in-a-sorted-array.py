class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        suffix = [0] * (len(nums))
        prefix = []
        new = [0] * (len(nums))
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            prefix.append(curr)
        curr = 0
        for i in range(len(nums)-1, -1, -1):
            curr += nums[i]
            suffix[i] += curr      
        for j in range(len(nums)):
            ans = (nums[j] * j) - prefix[j] + suffix[j] - ((len(nums)- 1 - j)*nums[j]) 
            new[j] = ans
        return new
        
                
        
        