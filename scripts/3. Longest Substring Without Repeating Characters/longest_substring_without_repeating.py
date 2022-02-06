class Solution(object):
    def lengthOfLongestSubstring(self, s):
        curr_max_len = 0
        substring = ""
        for i in s:
            if i in substring:
                substring = substring.split(i)[1] + i
            else:
                substring += i

            if (len(substring) > curr_max_len):
                curr_max_len = len(substring)
            
        return curr_max_len