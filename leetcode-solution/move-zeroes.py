class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        while nums[i] != 0 and i < len(nums)-1:
            i +=1 
        j = i+1
        while j < len(nums):
            if nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i +=1
            j +=1        