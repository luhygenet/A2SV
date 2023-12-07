class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
     neg_list = []
     pos_list = []
     final=[]
     for i in range(len(nums)):
        if nums[i] > 0 :
            pos_list.append(nums[i])
        else:
            neg_list.append(nums[i])
     for i in range(int(len(nums)/2)):

         final.append(pos_list[i])
         final.append(neg_list[i])
     return final