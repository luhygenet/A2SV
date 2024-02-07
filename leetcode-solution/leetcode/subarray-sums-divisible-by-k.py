class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = [0] * k
        sum = 0
        for x in nums:
            sum += x%k
            count[sum % k] += 1
        res = count[0]
        for i in count:
            res += (i*(i-1))//2
        return res




        