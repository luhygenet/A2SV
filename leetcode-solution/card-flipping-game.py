class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        dontpick =set()
        for i in range (len(fronts)):
            if fronts[i] == backs[i]:
                dontpick.add(fronts[i])
        mini = float('inf')
        for number in (fronts + backs):
            if number not in dontpick:
                mini = min(mini, number)
        if mini == float('inf'):
            return 0
        return mini


                