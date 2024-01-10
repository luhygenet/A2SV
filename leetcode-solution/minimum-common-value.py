class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        j = 0
        i = 0 
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i] 
            if nums1[i] < nums2[j]:
                i +=1 
                continue
            if nums1[i] > nums2[j]:
                j +=1
                continue
        return -1
            


