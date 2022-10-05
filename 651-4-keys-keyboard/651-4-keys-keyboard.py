class Solution:
    def maxA(self, n: int) -> int:
        # say best[k] is the maximum number of A's that can be printed after k moves.
        # Thus, best[k] = max(best[k-1]+1, besk[k-2]+2, best[k-3]*2, best[k-4]*3 ...)
        best = [0, 1]
        for x in range(2, n+1):
            cur = max(best[x-1] + 1, best[x-2] + 2)
            for y in range(x-2):
                cur = max(cur, best[y] * (x-y-1))
            best.append(cur)
        return best[n]