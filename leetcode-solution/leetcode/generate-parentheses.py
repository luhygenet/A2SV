class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        ans = []
        count_open = 0
        count_close = 0
        def bt(i):
            nonlocal count_close
            nonlocal count_open
            if count_close > count_open:
                return
            if count_open > n:
                return  
            if len(ans) >= 2*n:
                s = ans[:]
                r = "".join(s)
                res.append(r)
                return
            
            ans.append("(")
            count_open += 1
            bt(i+1)
            o = ans.pop()
            if o == "(":
                count_open -= 1
            ans.append(")")
            count_close += 1
            bt(i+1)
            c = ans.pop()
            if c == ")":
                count_close -= 1
        bt(0)
        return res
        
        
            

