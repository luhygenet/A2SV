class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        res = []
        def ds(i):
            if i >= len(nums):
                final.append(res[:])
                return None
            res.append(nums[i])
            ds(i+1)
            res.pop()
            ds(i+1)
        ds(0)
        return final
        
            
