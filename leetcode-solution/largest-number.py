class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0:
            return "0"
        new = list(map(str, nums))
        print(new)
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                print(new[j] + new[j+1])
                print( new[j+1] + new[j])
                if new[j] + new[j+1] < new[j+1] + new[j]:
                    new[j], new[j+1] = new[j+1], new[j]

        return "".join(new) 