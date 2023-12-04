class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,num2]:
            return "0"
        res=[0]* (len(num1)+len(num2))
        num1 = num1[::-1]  
        num2 = num2[::-1]
        for i in range (len(num1)):
            for n in range (len(num2)):
                dig = int(num1[i])*int(num2[n])
                res[n + i] += dig
                res[n + i + 1] += ((res[n + i])//10)
                res[n + i] = (res[n + i]) % 10
        res, a = res[::-1],0
        while a<len(res) and res[a]==0:
            a+=1
        res=map(str,res[a:])
        return "".join(res)