class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        memo = [[None for x in range(n)] for x in range(m)]
        
        memo[0][0] = int(obstacleGrid[0][0] == 0)
        
        for i in range(1,m):
            memo[i][0] = int(obstacleGrid[i][0] == 0 and memo[i-1][0] == 1)
       
        for j in range(1, n):
            memo[0][j] = int(obstacleGrid[0][j] == 0 and memo[0][j-1] == 1)
            
        return self.path_count(m - 1, n - 1, obstacleGrid, memo)
    
    def path_count(self ,m ,n ,obstacleGrid ,memo):
        if memo[m][n] != None:
            return memo[m][n]
        
        if obstacleGrid[m][n] == 1:
            memo[m][n] = 0
            return 0
        
        else:
            memo[m][n] = self.path_count(m - 1, n ,obstacleGrid, memo) + self.path_count(m, n - 1 ,obstacleGrid , memo)
            return memo[m][n]
        
        

            
            
            
            