class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n != 0 and n & (n-1) == 0 and n == n & 1431655765