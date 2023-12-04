class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        mini=0
        for i in nums:
            if i == 1:
                count +=1
            else:
                count = 0
            mini = max(mini, count)
        return (mini)
