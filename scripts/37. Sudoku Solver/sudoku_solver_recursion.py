class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        return self.recur(0, 0, board)
    
    def next_cell(self, row, col, board):
        col += 1
        if col == 9: 
            col, row = 0, row + 1
        return row, col
    
    def recur(self, row, col, board):
        while board[row][col] != '.':
            if (col == 8) and (row == 8):
                try:
                    board[8][8] = list(set(board[0]) - set(board[8]))[0]
                except:
                    pass
                return board
            else:
                row, col = self.next_cell(row, col, board)

        for c in range(1,10):
            if self.isValid(row , col ,str(c), board):
                board[row][col] = str(c)
                if self.recur(row , col, board):
                    return True
        board[row][col] = '.'  
        return False

                          
    def isValid(self, row, col, value, board):
        # Checks for duplicate number in row
        if (board[row].count(value) != 0):
            return False

        for i in range(9):
            # Checks for duplicate number in column
            if (board[i][col] != value) or (i == row):
                continue
            else:
                return False

        quadrant_rows = [int(i + floor(row / 3) * 3) for i in [0,1,2]]
        quadrant_cols = [int(i + floor(col / 3) * 3) for i in [0,1,2]]


        for j in quadrant_rows:
            for k in quadrant_cols:
                # Checks for duplicate number in quadrant
                if (board[j][k] != value) or ((j == row) and (k == col)):
                    continue
                else:
                    return False

        # Otherwise just return valid 
        return True