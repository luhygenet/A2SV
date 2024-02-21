class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        sta = []
        ans = [-1] * len(nums)
        for i,n in enumerate(nums):
            while sta and nums[sta[-1]] < n:
                ans[sta.pop()] = n
            sta.append(i)
        for num in nums:
            while sta and nums[sta[-1]] < num:
                ans[sta.pop()] = num
        return ans

        
            

            

                