class OrderedStream:

    def __init__(self, n: int):
        self.list_val = [None]*n
        self.point = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.list_val[idKey - 1] = value
        ans = []
        while self.point < len(self.list_val) and self.list_val[self.point] is not None:
            ans.append(self.list_val[self.point])
            self.point +=1
        return ans
            


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)