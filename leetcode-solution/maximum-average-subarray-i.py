class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
            sum = 0
            for i in range(k):
                sum += nums[i]
          
            l = 0
            maxi = sum/k
            for r in range(k,len(nums)):
                sum -= nums[l]   
                sum += nums[r]
                l+=1
                maxi = max(maxi,sum/k)
                print(sum)
                
                
                  

            return maxi