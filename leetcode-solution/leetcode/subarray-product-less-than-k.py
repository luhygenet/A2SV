class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        subarrays = 0
        prd = 1
        start = 0

        for end in range(len(nums)):
            prd *= nums[end]

            while prd >= k and start <= end:
                prd //= nums[start]
                start += 1

            subarrays += end - start + 1

        return subarrays

            
            
            

