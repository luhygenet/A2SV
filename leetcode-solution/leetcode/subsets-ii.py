class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        res = []
        prev = -1
        def ds(i):
            nonlocal prev
            if i >= len(nums):
                final.append(res[:])
                return None
            prev = nums[i]
            res.append(nums[i])
            ds(i+1)
            while i <len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            res.pop()
            ds(i+1)
        ds(0)
        return final