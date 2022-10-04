class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n, MOD = len(pizza), len(pizza[0]), 10**9+7
        preSum = [[0] * (n+1) for _ in range(m+1)]
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                preSum[r][c] = preSum[r][c+1] + preSum[r+1][c] - preSum[r+1][c+1] + (pizza[r][c] == 'A')
        dp = [[[-1 for _ in range(n)] for _ in range(m)] for _ in range(k)]
        return self.dfs(m, n, k-1, 0, 0, dp, preSum)
    
    def dfs(self, m, n, k, r, c, dp, preSum):
        if preSum[r][c] == 0: return 0
        if k == 0: return 1
        if dp[k][r][c] != -1: return dp[k][r][c]
        
        ans = 0
        # cut in horizontal
        for nr in range(r+1, m):
            if preSum[r][c] > preSum[nr][c]:
                ans = (ans + self.dfs(m, n, k-1, nr, c, dp, preSum)) % (10**9+7)
        # cut in vertical
        for nc in range(c+1, n):
            if preSum[r][c] > preSum[r][nc]:
                ans = (ans + self.dfs(m, n, k-1, r, nc, dp, preSum)) % (10**9+7)
        
        dp[k][r][c] = ans
        return ans