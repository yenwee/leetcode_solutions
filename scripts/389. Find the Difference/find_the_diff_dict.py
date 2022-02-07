class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = list(t) + list(s)
        ans.sort()
        d = {}
        for index in range(len(ans)):
            if ans[index] not in d:
                d[ans[index]] = 1
            else:
                d[ans[index]] += 1
            
            if index == len(ans) - 1:
                return ans[index]
            
            if (ans[index] != ans[index + 1]) and (d[ans[index]] % 2 != 0):
                return ans[index]
