class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(i, j, m, n, grid)
        return res
    
    def dfs(self, i, j, m, n, grid):
        grid[i][j] = '#'
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i+dx, j+dy
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                self.dfs(ni, nj, m, n, grid)