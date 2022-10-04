class LogSystem:

    def __init__(self):
        self.logs = []
        self.g = {'Year': 4, 'Month': 7, 'Day': 10, 'Hour': 13, 'Minute': 16, 'Second': 19}

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        idx = self.g[gra]
        s, e = s[:idx], e[:idx]
        return [id for id, log in self.logs if s <= log[:idx] <= e]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)