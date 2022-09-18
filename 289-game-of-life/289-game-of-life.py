class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 00 dead(next) <- dead(current)
        # 01 dead(next) <- live(current)
        # 10 live(next) <- dead(current)
        # 11 live(next) <- live(current)
        
        # board[i][j] &  1 -- current state
        # board[i][j] >> 1 -- next state
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                lives = self.liveNeighbors(board, m, n, i, j)
                # In the beginning, every 2nd bit is 0
                # So we only need to care about when will the 2nd bit become 1
                if board[i][j] == 1 and lives >= 2 and lives <= 3:
                    board[i][j] = 3
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1   # Refresh next state
    
    def liveNeighbors(self, board, m, n, i, j):
        lives = 0
        for x in range(max(i-1,0), min(i+2,m)):
            for y in range(max(j-1,0), min(j+2,n)):
                lives += board[x][y] & 1
        lives -= board[i][j] & 1
        return lives