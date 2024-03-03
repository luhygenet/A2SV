class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def dfs(n,k):
            if n == 1:
                return 0
            
            count = 2 ** (n-1)

            if k > count//2:
                return 1 - dfs(n, k - (count//2))
            else:
                return dfs(n-1, k)

        return (dfs(n,k))