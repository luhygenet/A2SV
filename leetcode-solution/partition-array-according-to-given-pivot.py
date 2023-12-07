class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than = []
        equal_to = []
        greater_than = []
        res = []
        
        for i in range (len(nums)):
            if nums[i] < pivot:
                less_than.append(nums[i])
            elif nums[i] > pivot:
                greater_than.append(nums[i])
            else:
                equal_to.append(nums[i])
        for i in range (len(less_than)):
            res.append(less_than[i])
        for i in range (len(equal_to)):
            res.append(equal_to[i])
        for i in range (len(greater_than)):
            res.append(greater_than[i])
        return res

