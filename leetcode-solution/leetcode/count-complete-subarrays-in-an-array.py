class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        c = len(set(nums))
        count = 0
        for i in range(n):
            new_set = set()
            for j in range(i,n):
                new_set.add(nums[j])
                if len(new_set) == c:
                    count += 1
                elif len(new_set) > c:
                    break
        return count
            
            
