class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # left -> right
        for i in range(m):
            cur = 0
            for j in range(n):
                if grid[i][j] == 'W': cur = 0
                if grid[i][j] == 'E': cur += 1
                else: dp[i][j] += cur
        # right -> left
        for i in range(m):
            cur = 0
            for j in range(n-1, -1, -1):
                if grid[i][j] == 'W': cur = 0
                if grid[i][j] == 'E': cur += 1
                else: dp[i][j] += cur
        # up -> down
        for j in range(n):
            cur = 0
            for i in range(m):
                if grid[i][j] == 'W': cur = 0
                if grid[i][j] == 'E': cur += 1
                else: dp[i][j] += cur
        # down -> up
        for j in range(n):
            cur = 0
            for i in range(m-1, -1, -1):
                if grid[i][j] == 'W': cur = 0
                if grid[i][j] == 'E': cur += 1
                else: dp[i][j] += cur
        
        return max(dp[i][j] for i in range(m) for j in range(n))