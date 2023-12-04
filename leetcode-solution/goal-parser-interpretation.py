class Solution:
    def interpret(self, command: str) -> str:
        noi=""
        i = 0 
        while i < len(command):
            j = i+1
            if command[i] == "G":
                noi += "G"
            else:
                if command[j] == ")":
                    noi += "o"
                    i+=1
                elif command[j] == "a":
                    noi += "al"
                    i+=3
            i+=1
        return noi

