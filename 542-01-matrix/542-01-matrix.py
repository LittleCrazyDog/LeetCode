class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        seen = set()
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    seen.add((i, j))
        
        coords = [(0,1), (1,0), (0,-1), (-1,0)]
        distance = 1
        
        # BFS
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                for dx, dy in coords:
                    newX, newY = x + dx, y + dy
                    
                    if newX >= 0 and newX < m and newY >= 0 and newY < n and (newX, newY) not in seen:
                        mat[newX][newY] = distance
                        queue.append((newX, newY))
                        seen.add((newX, newY))
            
            distance += 1
        
        return mat