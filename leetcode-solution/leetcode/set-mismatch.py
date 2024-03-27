class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []
        for i in range(N):
            while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                corr = nums[i] - 1
                nums[i], nums[corr] = nums[corr], nums[i]
        for i in range(N):
            if nums[i] - 1 != i:
                ans.append(nums[i])
                ans.append(i+1)
                break
        return ans

