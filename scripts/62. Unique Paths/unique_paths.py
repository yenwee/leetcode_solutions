class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[None for x in range(n)] for x in range(m)]
        return self.path_count(m - 1, n - 1, memo)
    
    def path_count(self ,m ,n ,memo):
        if memo[m][n] != None:
            return memo[m][n]
        
        if m == 0 or n == 0:
            memo[m][n] = 1
            return 1
        
        else:
            memo[m][n] = self.path_count(m - 1, n , memo) + self.path_count(m, n - 1 , memo)
            return memo[m][n]
        
        

            
            
            
            