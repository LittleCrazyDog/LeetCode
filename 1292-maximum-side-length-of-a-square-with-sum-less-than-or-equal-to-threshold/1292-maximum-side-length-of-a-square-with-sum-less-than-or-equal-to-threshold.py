class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        res = 0
        m, n = len(mat), len(mat[0])
        preSum = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                preSum[i][j] = mat[i-1][j-1] + preSum[i-1][j] + preSum[i][j-1] - preSum[i-1][j-1]
                l, r = 1, min(i, j)
                while l <= r:
                    m = (l + r) // 2
                    curSum = preSum[i][j] - preSum[i-m][j] - preSum[i][j-m] + preSum[i-m][j-m]
                    if curSum <= threshold:
                        res = max(res, m)
                        l = m + 1
                    else:
                        r = m - 1
        return res