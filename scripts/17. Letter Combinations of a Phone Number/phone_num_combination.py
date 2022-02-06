class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d ={
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        if len(digits) == 0 :
            return []
        
        curr = []
        for alp in d[digits[0]]:
            curr.append(alp)
            
        dum = curr
        
        for digit in digits[1:]:
            dum = []
            for combination in d[digit]:
                dum = dum + [s + combination for s in curr]
            curr = dum
        return dum