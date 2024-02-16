class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        hashi = defaultdict(list)
        new = [0] * len(nums)
        for idx,num in enumerate(nums):
            hashi[num].append(idx)
        print(hashi)
        for key in hashi:
            prefix = [hashi[key][0]]
            print(prefix)
            for i in range(1,len(hashi[key])):
                prefix.append(prefix[-1] + hashi[key][i])
            
            for idx, num in enumerate(hashi[key]):
                if idx - 1 >= 0:
                    left = abs(prefix[idx-1] - (idx * num))
                else:
                    left = 0
                right = abs((prefix[-1] - prefix[idx]) - (len(hashi[key]) - idx - 1)*num)

                if len(hashi[key]) == 1: new[num] = 0
                else: new[num] = left + right
        return new


      
        