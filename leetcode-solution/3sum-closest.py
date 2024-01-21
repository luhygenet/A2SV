class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = nums[0] + nums [1] + nums[len(nums)-1] 
        nums.sort()

        for i in range(len(nums)-2):
            a = i + 1
            b = len(nums)-1

            while(a < b):
                curr_sum = nums[i] + nums[a] + nums [b]
                if curr_sum > target :
                    b -= 1
                else:
                    a +=1
                
                if abs(curr_sum - target)< abs(res-target):
                    res = curr_sum

                
        return res
                
            
        
