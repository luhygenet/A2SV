class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] == val:
                return 0
        i = 0 
        j = len(nums)-1
        k = 0
        nums.sort()
        while nums[j] == val and j >= i:
            j-=1
        while i <= j :
            if nums[i] == val:
                nums[i],nums[j] = nums[j],nums[i]
                
                j -= 1
                while nums[j] == val and j > i:
                    j-=1
            k += 1
            i += 1
        print(nums)
        return k