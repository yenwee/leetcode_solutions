class Solution(object):
    def convert(self, s, numRows):
        l = [''] * numRows
        curr = 0
        direction = 1

        if numRows == 1:
            return s
            
        for char in s:
            l[curr] += char
            curr += direction
            if curr in (0, numRows - 1):
                direction *= -1
        
        return ''.join(l)