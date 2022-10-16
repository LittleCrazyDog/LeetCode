class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        res = 1
        i = 3
        while n % 2 == 0:
            n //= 2
        while i*i <= n:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            res *= count + 1
            i += 2
        return res if n == 1 else res * 2