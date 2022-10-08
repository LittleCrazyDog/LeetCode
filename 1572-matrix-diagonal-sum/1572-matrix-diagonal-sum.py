class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for i in range(n):
            res += mat[i][i]
            res += mat[i][n-1-i]
        if n % 2 == 1:
            res -= mat[n//2][n//2]
        return res