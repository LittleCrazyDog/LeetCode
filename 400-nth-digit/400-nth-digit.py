class Solution:
    def findNthDigit(self, n: int) -> int:
        # Check the same-length ranges 1-9, 10-99, 100-999, 1000-9999, etc.
        n -= 1
        for digits in range(1, 11):
            first = 10**(digits-1)
            if n < 9 * first * digits:
                return int(str(first + n/digits)[n % digits])
            n -= 9 * first * digits