class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        dirs = [[-1,0],[-1,1],[-1,-1],[0,0],[0,1],[0,-1],[1,0],[1,1],[1,-1]]
        for i in range(m):
            for j in range(n):
                temp = [img[i+dx][j+dy] for dx, dy in dirs if 0 <= i+dx < m and 0 <= j+dy < n]
                res[i][j] = sum(temp) // len(temp)
        return res