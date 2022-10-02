class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        maximum = 0
        dp = defaultdict(int)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    dp[i, j, 0] = dp[i, j-1, 0] + 1
                    dp[i, j, 1] = dp[i-1, j, 1] + 1
                    dp[i, j, 2] = dp[i-1, j-1, 2] + 1
                    dp[i, j, 3] = dp[i-1, j+1, 3] + 1
                    maximum = max(maximum, dp[i, j, 0], dp[i, j, 1], dp[i, j, 2], dp[i, j, 3])
        return maximum