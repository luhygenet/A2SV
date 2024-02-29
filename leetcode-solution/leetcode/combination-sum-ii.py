class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        candidates.sort()
        path = []
        
        def bt(j,total):
            prev = -1
            if total == target:
                final.append(path[:])
                return
            if total > target:
                return
            for i in range(j,len(candidates)):
                if candidates[i] == prev:
                    continue
                prev = candidates[i]
                path.append(candidates[i])
                bt(i+1,total+candidates[i])
                path.pop()
        bt(0,0)
        return final

            

        