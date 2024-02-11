class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0,1), (1,0),(0,-1),(-1,0)]
        obs = set()
        current = 0
        ans  = 0
        x,y = 0,0

        for o,b in obstacles:
            obs.add((o,b))
    
        for c in commands:
            if c == -2:
                current = (current + 3)%4
            elif c == -1:
                current = (current + 1)%4
            else:
                dir_x,dir_y = directions[current] 
                for i in range(c):
                    nx , ny = x + dir_x, y +dir_y

                    if (nx,ny) in obs:
                        break
                    x, y= nx,ny
                    ans = max(ans, (x * x) + (y*y))
        return ans
