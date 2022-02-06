class Solution(object):
    def myAtoi(self, s):
        neg = 0
        pos = 0
        stripped = s.strip()
        ans = ''
        for char in stripped:
            if (neg == 0) and (pos == 0) and (ans == ''):
                if char == '-':
                    neg = 1
                    continue
                if char == '+':
                    pos = 1
                    continue
            if (char.isdigit()):
                ans += char
            else:
                break
        if ans == "" :
            return 0 
        if (int(ans) > 2**31 - 1) and (neg == 0) :
            ans = str(2**31 - 1)
        if (int(ans) > 2**31) and (neg == 1):
            ans = str(2**31)
        if neg == 1 :
            ans = -int(ans.lstrip())
        else:
            ans = int(ans.lstrip())
        
        return ans
        