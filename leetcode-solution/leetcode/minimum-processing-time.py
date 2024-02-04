class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse = True)
        tasks.sort()
        listi = []
        maxi = 0
        r = 0
        for i in range(len(processorTime)):
            print(processorTime[i])
            for j in range(4):
                
                sums = processorTime[i] + tasks[r]
                print(sums)
                maxi = max(maxi, sums)
                print(maxi)
                r+=1
            listi.append(maxi)
        return max(listi)


