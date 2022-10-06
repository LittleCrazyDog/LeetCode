class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = sum(([(c, i), (j, c), (i//3, j//3, c)]
                   for i, row in enumerate(board)
                   for j, c in enumerate(row)
                   if c != '.'), [])
        return len(seen) == len(set(seen))