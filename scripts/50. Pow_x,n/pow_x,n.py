class Solution(object):
    def myPow(self, x, n):
        # Can consider just use ** operator or python pow function
        if not n:
            return 1
        
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        if n % 2:
            return x * self.myPow(x, n-1)
        
        return self.myPow(x*x, n/2)