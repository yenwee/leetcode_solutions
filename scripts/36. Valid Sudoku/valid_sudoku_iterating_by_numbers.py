class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col in range(9):
                # Skip if empty cell
                if board[row][col] == '.':
                    continue
                else:
                    # Checks for duplicate number in row
                    if (board[row].count(board[row][col]) > 1):
                        return False
                
                    else:
                        for i in range(9):
                            # Checks for duplicate number in column
                            if (board[i][col] != board[row][col]) or (i == row):
                                continue
                            else:
                                return False
                        
                        quadrant_rows = [int(i + floor(row / 3) * 3) for i in [0,1,2]]
                        quadrant_cols = [int(i + floor(col / 3) * 3) for i in [0,1,2]]
                        
                        
                        for j in quadrant_rows:
                            for k in quadrant_cols:
                                # Checks for duplicate number in quadrant
                                if (board[j][k] != board[row][col]) or ((j == row) and (k == col)):
                                    continue
                                else:
                                    return False
            
        return True