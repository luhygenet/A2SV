class Solution:
    def decodeString(self, s: str) -> str:
        sta = []
        for i in range(len(s)):
            if s[i] != "]":
                sta.append(s[i])
            else:
                sub = ""
                while sta[-1] != "[":
                    sub = sta.pop() + sub
                sta.pop()
                nums_s = ""
                while sta and sta[-1].isdigit():
                    nums_s = sta.pop() + nums_s
                # for _ in range(nums_s):
                #     sta.append(sub)
                sta.append(int(nums_s) * sub)
        return "".join(sta)

            
                




                