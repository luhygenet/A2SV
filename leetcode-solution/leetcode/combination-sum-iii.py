class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = set()
        path = []
        seti = set()
        target = 0
        def bt(j):
            nonlocal target
            if len(path) == k and target == n:
                    ans.add(tuple(path[:]))
                    return None
            for i in range(j, 10):
                if target > n:
                    return
                if i in seti:  continue
                path.append(i)
                target += i
                seti.add(i)
                
                bt(i+1)
                path.pop()
                target -= i
                seti.remove(i)
                
        bt(1)
        return ans


