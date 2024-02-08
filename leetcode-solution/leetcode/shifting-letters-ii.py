class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        s_nums=list(map(ord,list(s)))
        new = [0] * (n + 1)
        for i in shifts:
            l = i[0]
            r = i[1]
            forward = i[2]
            if forward:
                new[l] += 1
                new[r + 1] -= 1
            else:
                new[l] += -1
                new[r + 1] -= -1   
        for i in range(1,len(new)):
            new[i] += new[i - 1]
        for idx,order in enumerate(s_nums):
            order += new[idx]
            s_nums[idx] = chr((order -97)%26 + 97)   
        return "".join(s_nums)
            

            
        


