class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows, cols = self.get_building_points(grid)
        x_median, y_median = self.get_median_coordinates(rows, cols)
        res = 0
        for x in rows: res += abs(x-x_median)
        for y in cols: res += abs(y-y_median)
        return res
    
    def get_building_points(self, grid):
        m, n = len(grid), len(grid[0])
        rows, cols = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        return rows, cols
    
    def get_median_coordinates(self, rows, cols):
        rows.sort()
        cols.sort()
        x_median, y_median = rows[len(rows)//2], cols[len(cols)//2]
        return x_median, y_median