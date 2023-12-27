class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            j = i
            for r in range(j+1,len(nums)):
                if nums[r] < nums[j]:
                    j = r
            nums[j], nums[i] = nums[i], nums[j]
        return nums