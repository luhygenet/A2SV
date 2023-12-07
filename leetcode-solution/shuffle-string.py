class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new=[]
        list_s= list(s)
        hash = {key: value for key, value in zip(indices, list_s)}
        for i in range (len(s)):
          new.append(hash[i])
        return "".join(new)
