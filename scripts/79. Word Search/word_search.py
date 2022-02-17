class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.recurse(board,word,-1, -1)

        
    def recurse(self, board, word, row, col): 
        # Returning True once all words are found on the board
        if word == "":
            return True
        
        # Initialization (Finding first letter across the board)
        if row == -1 and col == -1:
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] == word[0]:
                        board[row][col] = ""
                        if self.recurse(board, word[1:], row, col):
                            return True 
                        board[row][col] = word[0]
        
        # Finds the next letter by looking at the cell above
        if row + 1 <= len(board) - 1:                    
            if word[0] == board[row + 1][col]:
                board[row + 1][col] = ""
                if not self.recurse(board, word[1:], row + 1, col):
                    board[row + 1][col] = word[0]
                else:
                    return True
                
        # Finds the next letter by looking at the cell below        
        if row - 1 >= 0:    
            if word[0] == board[row - 1][col]:
                board[row - 1][col] = ""
                if not self.recurse(board, word[1:], row - 1, col):
                    board[row - 1][col] = word[0]
                else:
                    return True
                
        # Finds the next letter by looking at the cell at the left        
        if col - 1 >= 0:    
            if word[0] == board[row][col - 1]:
                board[row][col - 1] = ""
                if not self.recurse(board, word[1:], row, col - 1):
                    board[row][col - 1] = word[0]
                else:
                    return True
                
        # Finds the next letter by looking at the cell at the right    
        if col + 1 <= len(board[0]) - 1:  
            if word[0] == board[row][col + 1]:
                board[row][col + 1] = ""
                if not self.recurse(board, word[1:], row, col + 1):
                    board[row][col + 1] = word[0]
                else:
                    return True
        
        # After looking through all first letters across the board, if the words are not fully found, return False
        return False
                
