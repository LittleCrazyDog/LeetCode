class TicTacToe:
    
    # Record the number of moves for each rows, columns, and two diagonals
    # For each move, we -1 for each player 1's move and +1 for each player 2's move
    # Then we just need to check whether any of the recorded numbers equal to n or -n

    def __init__(self, n: int):
        self.row, self.col, self.diag, self.anti_diag, self.n = [0] * n, [0] * n, 0, 0, n

    def move(self, row: int, col: int, player: int) -> int:
        offset = player * 2 - 3
        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            self.diag += offset
        if row + col == self.n - 1:
            self.anti_diag += offset
        
        if self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 2
        if -self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 1
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)