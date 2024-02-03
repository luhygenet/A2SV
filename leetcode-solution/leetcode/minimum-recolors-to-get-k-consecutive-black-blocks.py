class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        op = 0
        for r in range(k):
            if blocks[r] == 'W':
                op += 1
        count = op
        for s in range(k,len(blocks)):
            if blocks[l] == 'W':
                op -= 1
            l += 1
            if blocks[s] == 'W':
                op += 1 
            count = min(count,op)
        return count

