class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            j = i+1
            while j < len(nums):
                if nums[i] + nums[j] < target:
                    count +=1
                j += 1
        return count