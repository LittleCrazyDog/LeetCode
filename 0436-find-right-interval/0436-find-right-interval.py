class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        l = sorted((e[0], i) for i, e in enumerate(intervals))
        res = []
        for e in intervals:
            r = bisect.bisect_left(l, (e[1],))
            res.append(l[r][1] if r < len(l) else -1)
        return res