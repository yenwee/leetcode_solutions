class Solution(object):
    def romanToInt(self, s):
        m = s.count("M")
        d = s.count("D")
        c = s.count("C")
        l = s.count("L")
        x = s.count("X")
        v = s.count("V")
        i = s.count("I")
        iv = s.count("IV")
        ix = s.count("IX")
        xl = s.count("XL")
        xc = s.count("XC")
        cd = s.count("CD")
        cm = s.count("CM")
     
        return 1000*m + 500*d + 100*c + 50 *l + 10*x + 5*v + i - 2*(iv+ix) - 20*(xl+xc) - 200*(cd+cm)