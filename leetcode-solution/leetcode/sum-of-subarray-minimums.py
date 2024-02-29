class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(-float("infinity"))
        n = len(arr)
        total = 0
        mono_stack = []
        MOD = 10**9 +7
        for i in range(n):
            while mono_stack and arr[i] < mono_stack[-1][0]:
                num,idx = mono_stack.pop()
                right = i - idx
                if mono_stack:
                    left = idx - mono_stack[-1][1] 
                else:
                    left = idx + 1
                total += (num *right*left)
            mono_stack.append((arr[i],i))
        return total % MOD
        
