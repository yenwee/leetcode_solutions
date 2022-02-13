class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        carry = 0
        curr = []
        for j in range(len(num2)):
            for i in range(len(num1)):
                    product = (ord(num1[i]) -ord('0')) * (ord(num2[j]) - ord('0')) + carry
                    if (i != len(num1) - 1) and (product >= 10):
                        carry = product // 10
                        product = product % 10
                    else:
                        carry = 0
                    curr.append(product * (10 ** (i+j)))    
        return str(sum(curr))