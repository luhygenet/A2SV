class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        hashi = defaultdict(lambda:0)
        sta = []
        n = len(temperatures)
        for i in range(n):
            while sta and sta[-1][0] < temperatures[i]:
                hashi[sta[-1][1]] = i - sta[-1][1]
                sta.pop()
            sta.append([temperatures[i],i])
        for i in range(len(temperatures)):
            temperatures[i] = hashi[i]
        return temperatures
            

            