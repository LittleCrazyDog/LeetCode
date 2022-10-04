class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n and grid2[i][j] == 1): return 1
            grid2[i][j] = 0
            res = grid1[i][j]
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                res &= dfs(i+di, j+dj)
            return res
        
        return sum(dfs(i, j) for i in range(m) for j in range(n) if grid2[i][j])