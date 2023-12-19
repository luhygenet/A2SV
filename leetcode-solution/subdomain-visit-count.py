class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        match = defaultdict(int)
        for i in cpdomains:
            splitted=i.split(' ')
            domains = splitted[-1].split('.')
            for i in range(len(domains)):  
                match['.'.join(domains[i:])] +=  int(splitted[0])
        result = []
        for key,value in match.items():
            result.append(str(value) + " " +str(key))
        return result
            
        
        print(match)

        
        