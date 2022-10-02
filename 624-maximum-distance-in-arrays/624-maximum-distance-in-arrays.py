class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res, curMin, curMax = 0, float('inf'), float('-inf')
        for a in arrays:
            res = max(res, max(a[-1]-curMin, curMax-a[0]))
            curMin, curMax = min(curMin, a[0]), max(curMax, a[-1])
        return res