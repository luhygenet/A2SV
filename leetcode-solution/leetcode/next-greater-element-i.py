class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashi = defaultdict(lambda:-1)
        sta = []
        for i in range(len(nums2)):
            while sta and nums2[i] > sta[-1][0]:
                hashi[sta[-1][0]] = nums2[i]
                sta.pop()
            sta.append([nums2[i],i])
        new =[]
        for i in range(len(nums1)):
            new.append(hashi[nums1[i]])
        return new
        

            
        

            