class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Greedy
        # 1. Sort intervals by ending value
        # 2. Only count valid intervals we need, and skip overlapping intervals
        points = sorted(points, key = lambda x: x[1])
        res, end = 0, float('-inf')
        for interval in points:
            if interval[0] > end:
                res += 1
                end = interval[1]
        return res