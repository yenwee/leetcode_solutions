class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = ['(']
        for i in range(2*n - 1):
            dummy = []
            for j in ans:
                if (j.count('(') > j.count(')')) and (j.count('(') < n):
                    dummy.append(j + '(')
                    dummy.append(j + ')')
                elif (j.count('(') < n):
                    dummy.append(j+ '(')
                else:
                    dummy.append(j+ ')')
                
                
            ans = dummy
        return ans