class Solution(object):
    def longestCommonPrefix(self, strs):
        longest = ""
        for c in zip(*strs):
            if len(set(c)) == 1:
                longest += c[0]
            else:
                break
        return longest