from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        original = deque(senate)
        curr = deque()
        lasts = deque()
        i = 0 
        flag = True
        while flag:
            while len(original) >= 1:
                if len(original) == 1:
                    curr.append(original.pop())
                elif len(curr) != 0 and curr[0] != original[0]:
                    lasts.append(curr.popleft())
                    original.popleft() 
                elif original[0] == original[1]:
                    a = original.popleft()
                    curr.append(a)
                else:
                    r = original.popleft()
                    lasts.append(r)
                    original.popleft()
            while len(lasts) != 0:
                ap = lasts.popleft()
                curr.append(ap)
            if curr.count("D") == len(curr) or curr.count("R") == len(curr):
                print("yes")
                flag = False
            else:
                original = curr
                curr = deque()
        if curr.pop() == "R":
            return "Radiant"
        else:
            return "Dire"



        