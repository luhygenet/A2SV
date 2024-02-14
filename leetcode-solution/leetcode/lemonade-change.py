class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        numFive = 0
        numTen = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                numFive += 1
            elif bills[i] == 10:
                if numFive:
                    numFive -= 1
                    numTen += 1
                else:
                    return False
            elif bills[i] == 20:
                if numTen >= 1 and numFive >= 1:
                    numTen -= 1
                    numFive -= 1
                elif numFive >= 3:
                    numFive -= 3
                else:
                        return False
                
        return True

                        


                

            