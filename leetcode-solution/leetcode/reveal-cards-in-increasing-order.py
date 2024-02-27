from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]: 
        deck.sort(reverse = True)
        res = deque()
        for i in deck:
            if len(res) > 1:
                res.rotate(1)
            res.appendleft(i)
        return res
        