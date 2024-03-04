class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        ans = 0
        def bt(left,right,turn):
            # nonlocal nums
            nonlocal ans
            if left > right:
                return 0
            if turn:
                option1 = nums[left] + bt(left + 1, right,not turn)
                option2 = nums[right] + bt(left, right - 1, not turn)
                return max(option1,option2)
            else:
                option1 = -nums[left] + bt(left + 1, right,not turn)
                option2 = -nums[right] + bt(left, right - 1, not turn)
                return min(option1,option2)
        x = bt(0,len(nums)-1,True)
        return x >= 0

