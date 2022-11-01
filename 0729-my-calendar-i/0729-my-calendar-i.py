from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.arr = SortedList()

    def book(self, start: int, end: int) -> bool:
        q1 = SortedList.bisect_right(self.arr, start)
        q2 = SortedList.bisect_left(self.arr, end)
        if q1 == q2 and q1 % 2 == 0:
            self.arr.add(start)
            self.arr.add(end)
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)