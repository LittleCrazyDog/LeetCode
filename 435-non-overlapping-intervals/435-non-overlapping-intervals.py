class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Greedy: always pick the interval with the earliest end time
        end, cnt = float('-inf'), 0
        for s, e in sorted(intervals, key=lambda x:x[1]):
            if s >= end:
                end = e
            else:
                cnt += 1
        return cnt