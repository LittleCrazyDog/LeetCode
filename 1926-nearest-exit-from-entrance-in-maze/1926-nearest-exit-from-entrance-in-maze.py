class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        x, y = entrance
        m, n = len(maze), len(maze[0])
        infi = 1e5
        reached = lambda p, q: (not p==x or not q==y) and (p==0 or q==0 or p==m-1 or q==n-1)
        q = deque([(x, y, 0)])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            row, col, dist = q.popleft()
            for dx, dy in directions:
                r, c = row+dx, col+dy
                if r < 0 or c < 0 or r==m or c==n or maze[r][c]=='+':
                    continue
                if reached(r, c):
                    return dist+1
                maze[r][c] = '+'
                q.append((r, c, dist+1))
        return -1