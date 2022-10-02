class Solution:
    def findDerangement(self, N: int) -> int:
        MOD = 10**9+7
        X, Y = 1, 0
        for n in range(2, N+1):
            X, Y = Y, (n-1) * (X+Y) % MOD
        return Y