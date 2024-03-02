class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        oper = 0
        compare = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > compare:
                ans = ceil(nums[i]/compare)
                oper += ans - 1
                compare = floor(nums[i]/ans)
            else: 
                compare = nums[i]
        return oper
            

            



            
