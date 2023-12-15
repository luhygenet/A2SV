class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        newlist=[]
        sp=set(spaces)
        n=len(s)
        for i in range (n):
            if i in sp:
                newlist.append(" ")
            newlist.append(s[i])
        return "".join(newlist)