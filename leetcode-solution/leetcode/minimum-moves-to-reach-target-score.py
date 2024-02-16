class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        integer = target
        count = 0
        maxD = maxDoubles
        while maxD and integer > 1:
            if integer % 2 != 0:
                integer -=1
                count += 1
            elif integer % 2 == 0 and maxD:
                integer /= 2
                count += 1
                maxD -= 1
        if integer > 1:
                count += int(integer) - 1
        return count


            