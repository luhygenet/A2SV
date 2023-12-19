class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numToInd = {}
        for ind,value in enumerate(nums):
            numToInd[value] = ind

        for initial,final in operations:
            index = numToInd[initial]
            nums[index] = final
            numToInd[final] = index
        return nums