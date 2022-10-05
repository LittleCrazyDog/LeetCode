class Solution:
    def minSteps(self, n: int) -> int:
        def factors(n):
            d = 2
            while d * d <= n:
                while n % d == 0:
                    n //= d
                    yield d
                d += 1
            if n > 1:
                yield n
        return sum(factors(n))