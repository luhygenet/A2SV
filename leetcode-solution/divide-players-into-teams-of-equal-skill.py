class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        l = 0
        r = len(skill) - 1
        mini = skill[l] + skill[r]
        print(mini)
        chemistry = 0
        while l < r:
            if skill[l] + skill[r] != mini:
                return -1
            chemistry += skill[l] * skill[r]
            l += 1
            r -= 1
            
            print(chemistry)
        return chemistry
        

            