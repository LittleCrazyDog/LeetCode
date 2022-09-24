class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = math.floor((2*n + 0.25)**0.5 - 0.5)
        return rows