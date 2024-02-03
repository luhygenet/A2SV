class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       l = 0
       sumi = 0
       count = float('inf')
       for r in range(len(nums)):
           sumi += nums[r]
           while sumi>=target :
               count = min(count, r - l + 1)
               sumi -= nums[l]
               l+=1 
       return 0 if count == float('inf') else count
    
           
          
       return count
           


           


       return (count)