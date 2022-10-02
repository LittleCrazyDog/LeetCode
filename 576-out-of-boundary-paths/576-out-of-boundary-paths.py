class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        dp = [[[-1]*(maxMove+1) for _ in range(n+1)] for _ in range(m+1)]
        
        def solve(i, j, maxMove):
            if maxMove < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            
            # if the dp array at this position contains some value (not -1) then it means it has happen
            # computed earlier, so we don't need to compute again, hence return whatever value is present in dp.
            if dp[i][j][maxMove] != -1:
                return dp[i][j][maxMove]
            
            # otherwise compute the value
            a = solve(i-1, j, maxMove-1)
            b = solve(i+1, j, maxMove-1)
            c = solve(i, j-1, maxMove-1)
            d = solve(i, j+1, maxMove-1)
            
            # store the computed value in dp array so that we do not need to compute it again when the same
            # input occurs again
            dp[i][j][maxMove] = a + b + c + d
            
            return dp[i][j][maxMove]
        
        return solve(startRow, startColumn, maxMove) % (10**9+7)