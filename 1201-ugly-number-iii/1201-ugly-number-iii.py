class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        l, r = 1, 2*10**9+1
        while l < r:
            mid = (l + r) // 2
            if self.ok(a, b, c, n, mid):
                r = mid
            else:
                l = mid + 1
        return l
    
    def ok(self, a, b, c, n, x):
        return x // a + x // b + x // c - x // lcm(a, b) - x // lcm(a, c) - x // lcm(b, c) + x // lcm(a, b, c) >= n