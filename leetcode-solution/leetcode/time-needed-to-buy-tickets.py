class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        inds = []
        for i in range(len(tickets)):
            inds.append(i)
        sold = deque(inds)
        ticket = 0
        while True:
            if tickets[k] == 0:
                return ticket
            else:
                pops = sold.popleft()
                if tickets[pops] == 0 and pops != k:
                    pass
                elif tickets[pops] == 0 and pops == k:
                    return ticket
                else:
                    ticket += 1
                    tickets[pops] -= 1
                    sold.append(pops)
