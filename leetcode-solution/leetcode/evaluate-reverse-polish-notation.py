class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        seti = {"+","-","*","/"}
        sta = []
        ans = 0
        for i in range(n):
            if tokens[i] == "+":
                one = sta.pop()
                two = sta.pop()
                sta.append(one + two)
            elif tokens[i] == "-":
                one = sta.pop()
                two = sta.pop()
                sta.append(two - one)
            elif tokens[i] == "*":
                one = sta.pop()
                two = sta.pop()
                sta.append(two * one)
            elif tokens[i] == "/":
                one = sta.pop()
                two = sta.pop()
                sta.append(int(two / one))
            else:
                sta.append(int(tokens[i]))
        return(sta[-1])

                
                
                