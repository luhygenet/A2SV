class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
       winners = defaultdict(int) 
       losers = defaultdict(int)
       loser_onematch = []
       final_winners = []
       
       for i in range(len(matches)):
           losers[matches[i][1]] +=1
       for i in losers:
           if losers[i] == 1:
               loser_onematch.append(i)
       loser_onematch.sort()
       for i in range(len(matches)):
           winners[matches[i][0]] +=1
       for i in winners:
           if i not in losers:
               final_winners.append(i)
       final_winners.sort()
       return (final_winners, loser_onematch)


        