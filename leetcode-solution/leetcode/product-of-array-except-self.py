class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [0] * len(nums)
        news = [0] * len(nums)
        curr = 1
        for i in range(len(nums)):
            curr*=nums[i]
            prefix.append(curr)
        curr = 1
        for i in range(len(nums) - 1 , -1, -1):
            curr*=nums[i]
            suffix[i] = curr
        suffix.append(1)
        for i in range(len(nums)):
            news[i] = prefix[i] * suffix[i + 1]
        return news
            

        
        

            
