class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        while True:
            # 1. Check
            crush = set()
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if j > 1 and board[i][j] and board[i][j] == board[i][j-1] == board[i][j-2]:
                        crush |= {(i, j), (i, j-1), (i, j-2)}
                    if i > 1 and board[i][j] and board[i][j] == board[i-1][j] == board[i-2][j]:
                        crush |= {(i, j), (i-1, j), (i-2, j)}
            
            # 2. Crush
            if not crush: break
            for i, j in crush: board[i][j] = 0

            # 3. Drop
            for j in range(len(board[0])):
                idx = len(board) - 1
                for i in reversed(range(len(board))):
                    if board[i][j]:
                        board[idx][j] = board[i][j]
                        idx -= 1
                for i in range(idx+1):
                    board[i][j] = 0
        return board