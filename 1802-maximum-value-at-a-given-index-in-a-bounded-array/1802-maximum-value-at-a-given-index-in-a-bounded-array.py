class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def test(a):
            b = max(a - index, 0)
            res = (a + b) * (a - b + 1) // 2
            b = max(a - ((n - 1) - index), 0)
            res += (a + b) * (a - b + 1) // 2
            return res - a
        maxSum -= n
        l, r = 0, maxSum
        while l < r:
            m = (l + r + 1) // 2
            if test(m) <= maxSum:
                l = m
            else:
                r = m - 1
        return l + 1