class RecentCounter:

    def __init__(self):
        self.requests = []
        self.remove = 0
        self.range = 0

    def ping(self, t: int) -> int:
        while self.remove < len(self.requests) and (t - 3000) > self.requests[self.remove]:
            self.remove += 1
        self.requests.append(t)
        return len(self.requests) - self.remove
        

        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)