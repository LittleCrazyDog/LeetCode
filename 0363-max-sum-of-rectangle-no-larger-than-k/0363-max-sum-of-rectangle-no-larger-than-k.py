class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]
        res = float('-inf')
        for y1 in range(n):
            for y2 in range(y1, n):
                arr = [matrix[x][y2] - (matrix[x][y1-1] if y1 > 0 else 0) for x in range(m)]
                res = max(res, self.maxSumSubarray(arr, k))
        return res
    
    def maxSumSubarray(self, arr, k):
        sub_s_max = float('-inf')
        s_curr = 0
        prefix_sums = [float('inf')]
        for x in arr:
            bisect.insort(prefix_sums, s_curr)
            s_curr += x
            i = bisect.bisect_left(prefix_sums, s_curr - k)
            sub_s_max = max(sub_s_max, s_curr - prefix_sums[i])
        return sub_s_max