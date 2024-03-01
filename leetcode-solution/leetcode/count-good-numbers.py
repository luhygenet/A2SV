class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return (pow(5,(n + 1)//2,1000000007)*pow(4,n//2,1000000007))%1000000007
        MOD = 10**9 + 7
        if n == 1:
            return 5
        else:
            if n % 2 == 0:
                ans = (5**(n//2))*(4 **(n//2)) % MOD
    
            else:
                ans = (5**((n//2)+1)) * (4 **(n//2)) % MOD
        return ans 
