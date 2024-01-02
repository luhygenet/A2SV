class Solution:
    def smallestNumber(self, num: int) -> int:
        res=[]
        s = str(num)
        for i in range(len(s)):
            res.append(s[i])
        res.sort()
        if res[0] == '-':
            resi = res[1:]
            resi.sort(reverse=True)
            i = 1
            return (int('-' +"".join(resi)))
        
        if res[0] == '0':
            j = 0
            print(res)
            while res[j] == '0'and j <len(s)-1:
                j+=1
            res[j],res[0] = res[0],res[j]
        print("".join(res))
        return (int("".join(res)))
        
       
            
            