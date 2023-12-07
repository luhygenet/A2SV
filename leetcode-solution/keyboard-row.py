class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        same_row=[]
        same_row_words = {"q": 1, "w": 1, "e": 1, "r": 1, "t": 1, "y": 1, "u": 1, "i": 1, "o": 1,"p": 1, "a": 2, "s": 2, "d": 2, "f": 2, "g" :2, "h": 2, "j": 2, "k": 2, "l": 2,"z": 3 ,"x": 3, "c": 3, "v": 3, "b": 3, "n": 3, "m": 3 }
        for i in range (len(words)):
            flag = True
            start_num = same_row_words[(words[i][0]).lower()]
            for j in range (len(words[i])):
                    if same_row_words[(words[i][j]).lower()] != start_num:
                        flag = False
                        break
            if flag:
                    same_row.append(words[i])
        return same_row  

                    
