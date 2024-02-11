class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        state = [[0] * n for i in range(m)]
       
        GUARD = 1
        WALL = 2
        USED = 3
        for x,y in guards:
            state[x][y] = GUARD
        for x,y in walls:
            state[x][y] = WALL

        for i in range(m):
            current = 0
            for j in range(n):
                if state[i][j] == GUARD:
                    current = USED
                elif state[i][j] == WALL:
                    current = 0
                elif state[i][j] == 0:
                    if current == USED:
                        state[i][j] = USED
        for i in range(m):
            current = 0
            for j in range(n-1, -1, -1):
                if state[i][j] == GUARD:
                    current = USED
                elif state[i][j] == WALL:
                    current = 0
                elif state[i][j] == 0:
                    if current == USED:
                        state[i][j] = USED
        for j in range(n):
            current = 0
            for i in range(m):
                if state[i][j] == GUARD:
                    current = USED
                elif state[i][j] == WALL:
                    current = 0
                elif state[i][j] == 0:
                    if current == USED:
                        state[i][j] = USED
        for j in range(n):
            current = 0
            for i in range(m-1, -1, -1):
                if state[i][j] == GUARD:
                    current = USED
                elif state[i][j] == WALL:
                    current = 0
                elif state[i][j] == 0:
                    if current == USED:
                        state[i][j] = USED
        count = 0
        for i in range(m):
            for j in range(n):
                if state[i][j] == 0:
                    count += 1
        print(state)
        return count
                
        #for i in range(len(guards)):
         #   new[guards[l]][guards[r]]
                
        