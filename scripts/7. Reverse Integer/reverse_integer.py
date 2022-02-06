class Solution(object):
    def reverse(self, x):
        if x == 0 :
            return 0

        if x < 0 :
            neg = 1
        else:
            neg = 0
        
        if neg == 1 :
            ans = ((str(x))[1:])[::-1]
            ans = ans.lstrip('0')
            ans = '-' + ans
            
        else:
            ans = str(x)[::-1]
            ans = ans.lstrip('0')
        
        if (int(ans) >= -2**31) and (int(ans) <= 2**31 -1):
            return ans
        else:
            return 0
        