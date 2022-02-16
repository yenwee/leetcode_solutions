class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = set()
        c = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in r:
                    matrix[i][j] = 0
                    
                elif j in c:
                    matrix[i][j] = 0