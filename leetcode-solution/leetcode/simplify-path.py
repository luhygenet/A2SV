class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        print(paths)
        stack = []
        for diri in paths:
            if diri == "..":
                if stack:
                    stack.pop()
            elif diri != "." and diri != "":
                stack.append(diri)
        return "/" + "/".join(stack)