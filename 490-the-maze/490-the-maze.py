class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        Q = deque([start])
        n = len(maze)
        m = len(maze[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        maze[start[0]][start[1]] = 2
        while Q:
            i, j = Q.popleft()
            
            if i == destination[0] and j == destination[1]:
                return True
            
            for x, y in dirs:
                row = i + x
                col = j + y
                while 0 <= row < n and 0 <= col < m and maze[row][col] != 1:
                    row += x
                    col += y
                row -= x
                col -= y
                if maze[row][col] == 0:
                    Q.append([row, col])
                    maze[i][j] = 2
        
        return False