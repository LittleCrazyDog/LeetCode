class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 0, 1
        ans = []
        for _ in range(m*n):
            if not 0 <= x + dx < m or not 0 <= y + dy < n or matrix[x+dx][y+dy] == '*':
                dx, dy = dy, -dx
            ans.append(matrix[x][y])
            matrix[x][y] = '*'
            x, y = x + dx, y + dy
        return ans