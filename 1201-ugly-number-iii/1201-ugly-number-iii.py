class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def ok(x):
            return x // a + x // b + x // c - x // lcm(a, b) - x // lcm(a, c) - x // lcm(b, c) + x // lcm(a, b, c) >= n
        l, r = 1, 2*10**9+1
        while l < r:
            mid = (l + r) // 2
            if ok(mid):
                r = mid
            else:
                l = mid + 1
        return l