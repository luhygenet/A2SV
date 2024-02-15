class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        tot = 0
        hashi = defaultdict(int)
        print(hashi)
        for i in range(len(answers)):
            rab = answers[i]
            if rab == 0:
                tot += 1
            else:
                hashi[rab] += 1
                if hashi[rab] == 1:
                    tot += rab + 1
                elif hashi[rab] %  (rab + 1) == 0:
                    print(hashi[rab] %  (rab + 1))
                    hashi[rab] = 0
        return tot
        

