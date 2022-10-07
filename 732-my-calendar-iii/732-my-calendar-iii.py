class MyCalendarThree:

    def __init__(self):
        self.seg = defaultdict(int)
        self.lazy = defaultdict(int)
        
    def book(self, start: int, end: int) -> int:
        def update(s, e, l=0, r=10**9, ID=1):
            if r <= s or e <= l: return
            if s <= l < r <= e:
                self.seg[ID] += 1
                self.lazy[ID] += 1
            else:
                m = (l + r) // 2
                update(s, e, l, m, 2*ID)
                update(s, e, m, r, 2*ID+1)
                self.seg[ID] = self.lazy[ID] + max(self.seg[2*ID], self.seg[2*ID+1])
        update(start, end)
        return self.seg[1]


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)