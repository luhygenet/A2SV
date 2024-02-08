class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashi = defaultdict(int)
        hashi[0] += 1
        ans = 0
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            if (sums) - k in hashi:
                ans += hashi[(sums) - k]
            hashi[sums] += 1
        return ans






