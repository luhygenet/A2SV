class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        final = []
        def backtrack(i,path):
            if len(path) == k:
                final.append(path[:])
                return
            for i in range(i, n + 1):
                path.append(i)
                backtrack(i+1,path)
                path.pop()
        backtrack(1,[])
        return final            