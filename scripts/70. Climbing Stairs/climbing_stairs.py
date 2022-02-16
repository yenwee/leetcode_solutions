class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [None] * n
        return self.dynamic(n - 1, memo)
        
    def dynamic(self, n , memo):
        if memo[n] != None:
            return memo[n]
        
        elif n == 0:
            return 1
        
        elif n == 1:
            return 2
        
        else:
            memo[n] = self.dynamic(n - 2, memo) + self.dynamic(n - 1, memo)
            return memo[n]
