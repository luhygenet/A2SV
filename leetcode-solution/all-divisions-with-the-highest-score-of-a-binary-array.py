class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)

        best = total
        score = total
        ans=[0]
        for left in range (n):
            if nums[left] == 0:
                score += 1
            else:
                score -=1
            if best == score:
                ans.append(left +1)
            elif best <score:
                best = score
                ans = [left+1]
        return ans
           