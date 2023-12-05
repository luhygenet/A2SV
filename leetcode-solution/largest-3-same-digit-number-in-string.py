class Solution:
    def largestGoodInteger(self, num: str) -> str:
        greatest=[]
        nums=[eval(i) for i in (list(num))]
        i = 0
        while i< len(nums):
            j=i
            while j< len(nums) and nums[j] == nums[i]:
                    if j - i == 2:
                        greatest.append(nums[i])
                        i=j
                        break
                    j+=1
            i+=1
        if greatest == []:
           return ("")
        maxi=str(max(greatest))
        return (maxi+maxi+maxi)
