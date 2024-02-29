class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []
        def bt(i,path, past):
            if len(path) == len(nums):
                final.append(path[:])
                return

            for j in range(len(nums)):
                if j in past: continue
                path.append(nums[j])
                past.add(j)
                bt(j+1,path,past)
                path.pop()
                past.remove(j)

        bt(0,[],set())
        return final