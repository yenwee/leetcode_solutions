class Solution(object):
    def intToRoman(self, num):
        remainder = num
        ans = ""
        if remainder >= 1000:
            m = remainder / 1000
            ans += ''.join(['M'] * m)
            remainder -= m * 1000
        if remainder < 1000:
            if remainder >= 900:
                remainder -= 900
                ans += ''.join(['CM'])
            else:
                d = remainder / 500
                ans += ''.join(['D'] * d)
                remainder -= d * 500
            if remainder < 500:
                if remainder >= 400:
                    remainder -= 400
                    ans += ''.join(['CD'])
                else:
                    c = remainder /100
                    ans += ''.join(['C'] * c)
                    remainder -= c * 100
                if remainder < 100:
                    if remainder >= 90:
                        remainder -= 90
                        ans += ''.join(['XC'])
                    else:
                        l = remainder / 50
                        ans += ''.join(['L'] * l)
                        remainder -= l * 50
                    if remainder < 50:
                        if remainder >= 40:
                            remainder -= 40
                            ans += ''.join(['XL'])
                        else:
                            x = remainder / 10
                            ans += ''.join(['X'] * x)
                            remainder -= x *10
                        if remainder < 10:
                            if remainder == 9:
                                remainder -= 9
                                ans += ''.join(['IX'])
                            else:
                                v = remainder / 5
                                ans += ''.join(['V'] * v)
                                remainder -= v * 5
                            if remainder < 5:
                                if remainder == 4:
                                    remainder -= 4
                                    ans += ''.join(['IV'])
                                else:
                                    ans += ''.join(['I'] * remainder)
         
        return ans