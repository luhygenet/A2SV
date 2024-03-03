class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        hashi = defaultdict(int)
        ans = 0
        pref = [0] * len(nums) 
        for i in range(len(requests)):
            pref[requests[i][0]] += 1
            if requests[i][1] + 1 < len(nums):
                pref[requests[i][1] + 1] -= 1
        for i in range(1,len(pref)):
            pref[i] += pref[i - 1]
     
        nums.sort(reverse = True)
        pref.sort(reverse = True)
        for i in range(len(pref)):
            ans += nums[i]*pref[i]
        return ans % (10**9 + 7)
        

