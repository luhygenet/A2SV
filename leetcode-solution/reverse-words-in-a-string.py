class Solution:
    def reverseWords(self, s: str) -> str:
        new=s.split(" ")
        res= [i for i in new if i !=""] 
        res.reverse()
        return " ".join(res)