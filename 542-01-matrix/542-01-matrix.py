class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
        
        visited = set()
        
        visited.update(queue)
        
        count = 0
        
        # BFS
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy
                    
                    if xx < 0 or xx == m or yy < 0 or yy == n:
                        continue
                    
                    if (xx, yy) in visited:
                        continue
                    
                    queue.append((xx, yy))
                    
                    visited.add((xx, yy))
                
                if mat[x][y] == 0:
                    mat[x][y] = 0
                else:
                    mat[x][y] = mat[x][y] + count - 1
            count += 1
        
        return mat