class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def check(speed):
            time_needed = 0
            for d in dist[:-1]:
                time_needed += ceil(d/speed)
            time_needed += dist[-1]/speed
            return time_needed <= hour
        l, r = 1, 10**7+1
        while l < r:
            m = (l + r) // 2
            if check(m): r = m
            else: l = m + 1
        return l if l <= 10**7 else -1