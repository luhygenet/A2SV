class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixsum = [nums[0]] 
        for i in range(1,len(nums)):
            self.prefixsum.append(nums[i] + self.prefixsum[i-1])
      
    def sumRange(self, left: int, right: int) -> int:
        print(right)
        r = self.prefixsum[right]
        l = self.prefixsum[left - 1] if left > 0 else 0
        return r - l 


        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)