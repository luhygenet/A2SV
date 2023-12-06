class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        #ghost_distance = inf 
        closest_ghost = inf
        my_distance = abs(target[0]) + abs(target[1])
        for i in range (len(ghosts)):
            x = abs(ghosts[i][0] - target [0])
            y = abs(ghosts[i][1] - target [1])
            ghost_distance = x + y
            closest_ghost = min(closest_ghost, ghost_distance)
        if closest_ghost <= my_distance:
            return False
        return True
        