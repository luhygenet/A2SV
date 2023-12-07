class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numbers=[]
        seen = []
        for i in range (len(nums)):
            if nums[i] not in seen:
                total = 0
                check = nums[i]
                for j in range(i,len(nums)):
                    if nums[j] == check:
                        total += 1
                if  total > len(nums)//3 :
                        numbers.append(nums[i])
                        seen.append(nums[i])
        return numbers
