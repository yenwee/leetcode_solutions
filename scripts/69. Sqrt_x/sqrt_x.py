class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        
        while end >= start:
            mid = (start + end) // 2
            if mid * mid > x:
                end = mid - 1
            elif mid * mid < x:
                start = mid + 1
            else:
                return mid
        
        return end
        
        