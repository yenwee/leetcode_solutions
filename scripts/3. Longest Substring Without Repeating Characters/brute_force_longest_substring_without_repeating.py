class Solution(object):
    def lengthOfLongestSubstring(self, s):
        curr_max_len = 0
        for x in range(0,len(s)):
            if (curr_max_len >= len(s) - x ):
                break
            substring = ""
            for i in range(x,len(s)):
                if s[i] in substring:
                    break
                else:
                    substring +=s[i]
            if (len(substring) > curr_max_len):
                curr_max_len = len(substring)
        return curr_max_len