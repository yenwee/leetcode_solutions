class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) - 1
        
        while start <= end:
            mid = (start + end) //2
            
            if matrix[mid][0] > target:
                end = mid - 1
            elif matrix[mid][-1] < target:
                start = mid + 1 
            else: 
                return target in matrix[mid]
        
        
        