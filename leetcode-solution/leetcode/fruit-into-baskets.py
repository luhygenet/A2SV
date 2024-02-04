class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruiti = defaultdict(int)
        l = 0
        total = 0
        final = 0
        for r in range(len(fruits)):
            fruiti[fruits[r]] += 1
            total += 1

            while len(fruiti) > 2:
                f = fruits[l]
                fruiti[f] -= 1
                total -= 1
                l += 1

                if not fruiti[f]:
                    fruiti.pop(f)
            final = max(final,total)
        
        return final
    
       

        