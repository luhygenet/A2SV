class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        path = []
        
        def bt(i,total):
            if total == target:
                final.append(path[:])
                return
            if total > target or i > len(candidates)-1:
                return None
            path.append(candidates[i])
            bt(i,total + candidates[i])
            path.pop()
            bt(i + 1, total)
        bt(0,0)
        return final
            

