class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new=[]
        for i in range (n):
            j = i + n 
            new.append(nums[i])
            new.append(nums[j])
        return new