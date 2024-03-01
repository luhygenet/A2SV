class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        sta = []
        currmin = nums[0]

        for k in range(1,len(nums)):
            while sta and sta[-1][0] < nums[k]:
                sta.pop()
            if sta and sta[-1][1] < nums[k] < sta[-1][0]:
                return True
            sta.append([nums[k],currmin])
            currmin = min(currmin,nums[k])
        return False

        

        