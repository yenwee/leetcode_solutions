#The original number is divisible by 9 if and only if the sum of its digits is divisible by 9
class Solution:
    def addDigits(self, num: int) -> int:
        return num if num == 0 else num % 9 or 9
        