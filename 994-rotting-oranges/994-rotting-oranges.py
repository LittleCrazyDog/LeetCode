class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
        minutes_passed = 0
        while q:
            minutes_passed += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                    nx, ny = x+dx, y+dy
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx,ny))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minutes_passed-1 if minutes_passed > 0 else 0