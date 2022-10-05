class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and visited[i][j] == False:
                    count += 1
                    self.bfs(grid, visited, i, j)
        return count
    
    def bfs(self, grid, visited, i, j):
        queue = deque([(i, j)])
        while queue:
            I, J = queue.popleft()
            for i, j in [(I-1,J),(I+1,J),(I,J-1),(I,J+1)]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1' and visited[i][j] == False:
                    visited[i][j] = True
                    queue.append((i,j))