class SummaryRanges:

    def __init__(self):
        self.intervals = []
        self.seen = set()

    def addNum(self, val: int) -> None:
        if val not in self.seen:
            self.seen.add(val)
            heapq.heappush(self.intervals, [val, val])

    def getIntervals(self) -> List[List[int]]:
        tmp = []
        while self.intervals:
            cur = heapq.heappop(self.intervals)
            if tmp and cur[0] <= tmp[-1][1]+1:
                tmp[-1][1] = max(tmp[-1][1], cur[1])
            else:
                tmp.append(cur)
        self.intervals = tmp
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()