class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if typed == name:
            return True
        if len(name)> len(typed):
            return False

        i = 0
        j = 0
        while j < len(typed):
            if i <len(name)  and typed[j] == name[i]:
                i += 1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
            j += 1
           
        return i == len(name)
