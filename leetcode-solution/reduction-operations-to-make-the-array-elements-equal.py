class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        op =set()
        count = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] in op:
                count += len(op)-1
            else:
                count +=len(op)
            op.add(nums[i])
        return count
            

