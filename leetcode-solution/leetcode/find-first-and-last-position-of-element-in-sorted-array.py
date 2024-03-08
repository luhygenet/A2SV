class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)
        begin = -1
        end = -1
        for i in range(len(nums)):
            if nums[i] == target:
                begin = i
                break
        l = begin
        while l != -1 and l < r:
            mid = l + ((r - l)//2)
            
            if nums[mid] == target:
                end = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid
        if begin != -1 and end == -1:
            end = begin
        return [begin,end]

            