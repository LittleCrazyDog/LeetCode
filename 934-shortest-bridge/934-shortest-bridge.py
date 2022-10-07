class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or (i, j) in seen or grid[i][j] != 1: return
            seen.add((i, j))
            q.append((i, j, 0))
            grid[i][j] = -1
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                dfs(x, y)
        
        seen, q, m, n = set(), deque(), len(grid), len(grid[0])
        for i, j in product(range(m), range(n)):
            if grid[i][j]:
                dfs(i, j)
                break
        
        while q:
            i, j, h = q.popleft()
            if grid[i][j] == 1:
                return h - 1
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= x < m and 0 <= y < n and (x, y) not in seen:
                    seen.add((x, y))
                    q.append((x, y, h+1))
        
        return -1