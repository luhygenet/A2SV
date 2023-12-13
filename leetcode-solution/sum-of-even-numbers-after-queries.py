class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        numsind = dict()
        evenind = dict()
        oddind = dict()
        even_sum = 0
        even_sums=[]
        for i in nums:
            if i%2 == 0:
                even_sum +=i  
        for i in range (len(nums)):
            numsind[i] = nums[i]
        indofnums = numsind.items()
        for key,val in indofnums:
            if val % 2 == 0:
                evenind[key] = val
            else:
                oddind[key] = val
        for valiq,indexq in queries:
            if indexq in evenind:
                minus = evenind[indexq]
                evenind[indexq] =  evenind[indexq] + valiq
                if evenind[indexq] % 2 == 0:
                    even_sum += valiq
                else:
                    even_sum -= minus
                    oddind[indexq] = evenind[indexq]
                    del evenind[indexq]
                even_sums.append(even_sum)
            else:
                oddind[indexq] =  oddind[indexq] + valiq
                print (oddind[indexq])
                if oddind[indexq] % 2 == 0:
                    even_sum += oddind[indexq]
                    evenind[indexq] = oddind[indexq]
                    del oddind[indexq]
                even_sums.append(even_sum)
        return even_sums

                    
            