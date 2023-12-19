class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pastHash ={}
        for i,n in enumerate (nums):
            diff = target - n
            if diff in pastHash:
                return (pastHash[diff],i)
            pastHash[n] = i

            
