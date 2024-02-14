class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # count = 0
        # pref = 0
        # i = 0
        # while pref < n:
        #     if i < len(nums) and nums[i] <= pref + 1:
        #         pref += nums[i]
        #         i += 1
        #     else:
        #         pref += pref + 1
        #         count += 1
        # return count
        count = 0
        pref = 0
        i = 0
        while pref < n:
            if i < len(nums) and nums[i] <= pref + 1:
                    pref += nums[i]
                    i += 1
            else:
                pref += pref + 1
                count += 1
        return count
    







            
            

        
