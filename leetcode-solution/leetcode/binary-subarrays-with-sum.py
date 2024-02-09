class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashi = defaultdict(int)
        hashi[0] += 1
        curr = 0
        count = 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr - goal in hashi:
                count += hashi[curr-goal]
            hashi[curr] += 1
        return count
            


       




        
        