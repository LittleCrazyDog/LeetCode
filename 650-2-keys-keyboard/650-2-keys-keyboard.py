class Solution:
    def minSteps(self, n: int) -> int:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return self.minSteps(n // i) + i
        return 0 if n == 1 else n