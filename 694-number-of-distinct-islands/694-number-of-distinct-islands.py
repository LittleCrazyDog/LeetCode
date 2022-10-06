class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        island_shapes = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i, j, positions, rel_pos):
            grid[i][j] = -1
            for direction in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                next_i, next_j = i + direction[0], j + direction[1]
                if (0 <= next_i < rows and 0 <= next_j < cols) and grid[next_i][next_j] == 1:
                    new_rel_pos = (rel_pos[0] + direction[0], rel_pos[1] + direction[1])
                    positions.append(new_rel_pos)
                    dfs(next_i, next_j, positions, new_rel_pos)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    positions = []
                    dfs(i, j, positions, (0, 0))
                    island_shapes.add(tuple(positions))
        
        return len(island_shapes)