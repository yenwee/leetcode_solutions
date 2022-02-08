class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool::
        seen = []
        # i = row index
        for i, row in enumerate(board):
            # j = column index, c = cell value
            for j, c in enumerate(row):
                # Skips if cell is empty, else records seen 'value' in column j,
                # seen 'value' in row i and seen 'value' in quadrant from (0,0) to (3,3)
                if c != '.':
                    seen += [(c,j),(i,c),(i/3,j/3,c)]
        # Return true if there is none duplicate value is seen in either row, column or quadrant
        return len(seen) == len(set(seen))