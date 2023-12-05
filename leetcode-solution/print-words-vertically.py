class Solution:
    def printVertically(self, s: str) -> List[str]:
        result=s.split()
        new=[]
        max=0
        for tot in result:
            if len(tot) > max:
                max=len(tot)
                res=tot
        for ind in range (len(res)):
            emp=[]
            for i in range (len(result)):
                if ind >= len(result[i]):
                    emp.append(" ")
                else:
                    emp.append(result[i][ind])
                    
            new.append("".join(emp))
        for i in range(len(new)):

            j=len(new[i])-1
            while j > -1:
                if new[i][j]!=" ":
                    new[i]= new[i][:j+1]
                    break
                j-=1
        return new