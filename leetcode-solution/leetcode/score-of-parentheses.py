class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for chr in s:
            if chr == '(':
                stack.append(0)
            else:
                up = stack.pop()
                if up == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2*up
        return (stack[-1])