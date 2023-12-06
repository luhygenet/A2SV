class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        new=[]
        for i in range (0,len(nums),2):
            for n in range (nums[i]):
                new.append(nums[i+1])
        return new







            